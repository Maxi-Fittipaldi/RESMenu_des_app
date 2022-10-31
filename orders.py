from flask import(Blueprint,
render_template, request, url_for, redirect,
send_from_directory, session, flash)
from RESMenu_des_app import db
from .login import *
bp = Blueprint('orders',__name__, url_prefix='/')

@bp.route("/cashier/orders")
@staff_login_required
@verif_required
@cashier_required
def cashier_orders():
    dTrans = db.session.execute("""
SELECT 
dt.producto_id,
dt.cabecera_id,
dt.cantidad,
dt.monto,
dt.estado AS dtEstado,
p.nombre,
p.descripcion,
p.precio
        FROM detalleTransaccion dt
        JOIN productos p
        ON p.id = dt.producto_id
        WHERE p.id = dt.producto_id
        """).all()
    cTrans = db.session.execute("""
    SELECT * FROM cabeceraTransaccion WHERE estado = "pendiente"
    """).all()
    return render_template("orders.html", dTrans=dTrans, cTrans=cTrans, session=session)

@bp.route("/cashier/orders/update/<int:id>", methods=["POST"])
@login_required
@verif_required
@cashier_required
def cashier_update(id):
    estado = request.form["estado"]
    if estado != "en_proceso" and estado != "cancelado":
        return redirect(url_for("orders.cashier_orders"))
    db.session.execute("""UPDATE cabeceraTransaccion
    SET estado=:e
    WHERE id = :id
    """,
    {
    "e" :estado,
    "id" :id
    })
    db.session.commit()
    flash("Operación realizada.", "success")
    return redirect(url_for("orders.cashier_orders"))

@bp.route("/chef/orders")
@staff_login_required
@verif_required
@chef_required
def chef_orders():
    dTrans = db.session.execute("""
SELECT 
dt.producto_id,
dt.cabecera_id,
dt.cantidad,
dt.monto,
dt.estado AS dtEstado,
p.nombre,
p.descripcion,
p.precio
        FROM detalleTransaccion dt
        JOIN productos p
        ON p.id = dt.producto_id
        WHERE p.id = dt.producto_id
        """).all()
    cTrans = db.session.execute("""
    SELECT * FROM cabeceraTransaccion WHERE estado = "en_proceso"
    """).all()
    return render_template("orders.html", dTrans=dTrans, cTrans=cTrans, session=session)

@bp.route("/chef/orders/update/<int:id>", methods=["POST"])
@login_required
@verif_required
@chef_required
def chef_update(id):
    estado = request.form["estado"]
    if estado != "completado":
        return redirect(url_for("orders.chef_orders"))
    db.session.execute("""UPDATE cabeceraTransaccion
    SET estado=:e
    WHERE id = :id
    """,
    {
    "e" :estado,
    "id" :id
    })
    db.session.commit()
    flash("Operación realizada.", "success")
    return redirect(url_for("orders.chef_orders"))

@bp.route("/admin/orders")
@staff_login_required
@verif_required
@admin_required
def admin_orders():
    dTrans = db.session.execute("""
SELECT 
dt.producto_id,
dt.cabecera_id,
dt.cantidad,
dt.monto,
dt.estado AS dtEstado,
p.nombre,
p.descripcion,
p.precio
        FROM detalleTransaccion dt
        JOIN productos p
        ON p.id = dt.producto_id
        WHERE p.id = dt.producto_id
        """).all()
    cTrans = db.session.execute("""
    SELECT * FROM cabeceraTransaccion
    """).all()
    return render_template("orders.html", dTrans=dTrans, cTrans=cTrans, session=session)

@bp.route("/admin/orders/update/<int:id>", methods=["POST"])
@login_required
@verif_required
@admin_required
def admin_update(id):
    estado = request.form["estado"]
    db.session.execute("""UPDATE cabeceraTransaccion
    SET estado=:e
    WHERE id = :id
    """,
    {
    "e" :estado,
    "id" :id
    })
    db.session.commit()
    flash("Operación realizada.", "success")
    return redirect(url_for("orders.admin_orders"))