from flask import(Blueprint,
render_template, request, url_for, redirect,
send_from_directory, session, flash)
from RESMenu_des_app import db
from .login import *
bp = Blueprint('orders',__name__, url_prefix='/')

@bp.route("/orders")
@staff_login_required
@verif_required
@staff_required
def orders():
# hacer dos queries:
# detalleTransaccion unión con productos
# cabecera transaccion
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

@bp.route("/orders/update/<int:id>", methods=["POST"])
@login_required
@verif_required
@staff_required
def update(id):
    if request.method == "POST":
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
        return redirect("/orders")
