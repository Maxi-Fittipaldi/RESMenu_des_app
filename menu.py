from flask import Blueprint, render_template, request, url_for, redirect, send_from_directory, session, flash
from RESMenu_des_app import db
from .login import *
bp = Blueprint('menu', __name__, url_prefix='/')

@bp.route("/menu", methods=['GET'])
@login_required
@verif_required
def menu():
    pendingOrder = db.session.execute("""
    SELECT * FROM cabeceraTransaccion
    WHERE usuario_id = :uid 
    AND 
    estado = "pendiente" LIMIT 1""",{"uid": session["id"]}).scalar()
    if pendingOrder == None:
        session["order?"] = False
    else:
        session["order?"] = True
    productos = db.session.execute("SELECT * FROM productos")
    return render_template("menu.html",productos=productos, session=session)

@bp.route("/menu/commit",methods=["POST"])
@login_required
@verif_required
def commit():
    json = request.json
    db.session.execute("""
    INSERT INTO
    cabeceraTransaccion (usuario_id,nro_mesa,estado)
    VALUES(:uid, :nm, :e)""",
    {"uid": session["id"],
    "nm":session["nTable"],
    "e": "pendiente"})
    db.session.commit()
    db.session.execute("""
    INSERT INTO detalleTransaccion
    VALUES((SELECT id
    FROM cabeceraTransaccion
    WHERE usuario_id = :uid AND estado = "pendiente"),
    :producto_id,
    :cantidad,
    (SELECT precio FROM productos WHERE id = :producto_id),
    "pendiente",
    3,
    "Sin comentarios"
    )
    """,
    [
    {"producto_id": val["product_id"],
     "cantidad": val["quantity"],
     "uid": session["id"]}
        for val in json["product_ids"]
     ])
    db.session.commit()
    session["order?"] = True
    return ("Success",204)
@bp.route("/menu/cancel", methods=["GET"])
@login_required
@verif_required
def cancel():
    db.session.execute("""UPDATE cabeceraTransaccion
        SET estado="cancelado"
        WHERE usuario_id = :id AND estado="pendiente"
        """,
        {
        "id" :session["id"]
        })
    db.session.commit()
    session["order?"] = False
    return redirect("/menu")
