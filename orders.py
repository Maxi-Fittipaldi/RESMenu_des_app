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
    if not "id" in session:
        return redirect("/login")
    if session["rol"] == "cliente":
            return redirect("/profile")
    if session["state"] == "pendiente":
        return redirect("/profile")
    orders = db.session.execute("""SELECT * FROM cabeceraTransaccion WHERE estado = "pendiente" """)
    return render_template("orders.html", cabeceras_transaccion=orders)

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
