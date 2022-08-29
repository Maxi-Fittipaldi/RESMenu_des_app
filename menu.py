from flask import Blueprint, render_template, request, url_for, redirect, send_from_directory, session, flash
from RESMenu_des_app import db
bp = Blueprint('menu', __name__, url_prefix='/')

@bp.route("/menu", methods=['GET'])
def menu():
    productos = db.session.execute("SELECT * FROM productos")
    return render_template("menu.html",productos=productos, session=session)
@bp.route("/menu/commit",methods=["POST"])
def commit():
    content_type = request.headers.get("Content-Type")
    json = request.json
    db.session.execute("""
    INSERT INTO 
    cabeceraTransaccion (usuario_id,nro_mesa,estado)
    VALUES(:uid, :nm, :e)""",
    {"uid": session["id"],
    "nm":session["nTable"],
    "e": "pendiente"})
    for x in json["product_ids"]:
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
        "Sin comentarios",
        )
        """,
        {
        "uid": session["id"],
        "producto_id": x["product_id"],
        "cantidad": x["quantity"],
        })
    db.session.commit()
    session["order?"] = True
    return redirect("/menu")
@bp.route("/menu/cancel", methods=["GET"])
def cancel():
    session["order?"] = False
    return redirect("/menu")
