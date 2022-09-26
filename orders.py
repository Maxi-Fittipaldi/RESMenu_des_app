from flask import(Blueprint,
render_template, request, url_for, redirect,
send_from_directory, session, flash)
from RESMenu_des_app import db
from .login import *
bp = Blueprint('orders',__name__, url_prefix='/')

@bp.route("/orders")
@login_required
@verif_required
@staff_required
def orders():
# hacer dos queries:
# detalleTransaccion unión con productos
# cabecera transaccion
    query = db.session.execute("""
SELECT 
ct.id,
ct.usuario_id,
ct.nro_mesa,
ct.fecha,
ct.estado AS ctEstado,
dt.producto_id,
dt.cabecera_id,
dt.cantidad,
dt.monto,
dt.ranking,
dt.comentarios,
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
        WHERE ct.estado = 'pendiente'
        """).all()
    return render_template("orders.html", query=query)

@bp.route("/orders/update/<int:id>", methods=["POST"])
@login_required
@verif_required
@staff_required
def update(id):
    if request.method == "POST":
        estado = request.form ["estado"]
        print(estado)
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
