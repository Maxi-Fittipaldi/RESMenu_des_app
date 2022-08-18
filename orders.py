from flask import(Blueprint,
render_template, request, url_for, redirect,
send_from_directory, session, flash)
from RESMenu_des_app import db
bp = Blueprint('orders',__name__, url_prefix='/')

@bp.route("/orders")
def orders():
    if not "id" in session:
        return redirect("/login")
    if session["state"] == "pendiente":
        return redirect("/profile")
    orders = db.session.execute("""SELECT * FROM cabeceraTransaccion""")
    return render_template("orders.html", orders=orders)
