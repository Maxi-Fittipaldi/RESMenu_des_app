from flask import (Blueprint, render_template, request, url_for,
                   redirect, send_from_directory,session, flash)
from RESMenu_des_app import db
from .login import *
bp = Blueprint('menu', __name__, url_prefix='/')

@bp.route("/menu", methods=['GET'])
@login_required
def menu():
    pendingOrder = db.session.execute("""
    SELECT * FROM cabeceraTransaccion
    WHERE cliente_id = :cid 
    AND 
    estado = "pendiente" LIMIT 1""",{"cid": session["cid"]}).scalar()
    if pendingOrder == None:
        productos = db.session.execute("SELECT * FROM productos WHERE estado='visible'")
        session["order?"] = False
    else:
        productos = db.session.execute("""
        SELECT 
ct.id,
ct.cliente_id,
ct.fecha,
ct.estado AS ctEstado,
dt.producto_id,
dt.cantidad,
dt.monto,
dt.estado AS dtEstado,
p.nombre,
p.descripcion,
p.disponibilidad_desde,
p.disponibilidad_hasta,
p.precio,
p.propietario,
p.estado AS pEstado
        FROM cabeceraTransaccion ct
        JOIN detalleTransaccion dt
        ON dt.cabecera_id = ct.id
        JOIN productos p
        ON p.id = dt.producto_id
        WHERE ct.cliente_id = :cid
        AND ct.estado = 'pendiente'
        """,{"cid":session["cid"]})
        session["order?"] = True
    return render_template("menu.html",productos=productos, session=session)

@bp.route("/menu/commit",methods=["POST"])
@login_required
def commit():
    try:
        json = request.json
        product_ids = json["product_ids"]
        for x in product_ids:
            assert int(x["quantity"]) > 0
            assert int(x["product_id"]) > 0
    except ValueError:
        flash("Transacción inválida")
        return redirect("/menu")
    db.session.execute("""
    INSERT INTO
    cabeceraTransaccion (cliente_id,estado)
    VALUES(:cid, :e)""",
    {"cid": session["cid"],
    "e": "pendiente"})
    db.session.commit()
    db.session.execute("""
    INSERT INTO detalleTransaccion
    VALUES((SELECT id
    FROM cabeceraTransaccion
    WHERE cliente_id = :cid
     AND estado = "pendiente"),
    :producto_id,
    :cantidad,
    (SELECT precio FROM productos WHERE id = :producto_id),
    "pendiente")
    """,
    [
    {"producto_id": val["product_id"],
    "cantidad": val["quantity"],
    "cid": session["cid"]}
        for val in json["product_ids"]
    ])
    db.session.commit()
    session["order?"] = True
    return ("Success",204)

@bp.route("/menu/cancel", methods=["GET"])
@login_required
def cancel():
    db.session.execute("""UPDATE cabeceraTransaccion
        SET estado="cancelado"
        WHERE cliente_id = :cid AND estado="pendiente"
        """,
        {
        "cid" :session["cid"]
        })
    db.session.commit()
    session["order?"] = False
    return redirect(url_for("menu.menu"))
