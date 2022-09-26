from flask import Blueprint, render_template, request, url_for, redirect, send_from_directory, session, flash
from RESMenu_des_app.misc.encrypt import *
from RESMenu_des_app import db
from .login import *
bp = Blueprint('profile', __name__, url_prefix='/')
@bp.route("/profile")
@login_required
def profile():
    return render_template("profile.html", session=session)


@bp.route("/profile/update",  methods=['POST'])
@login_required
@verif_required
def update():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        password = request.form["password"]
        passwordEncrypted = encrypt(password)
        if len(nombre) < 2 or len(apellido) < 2 or len(password) < 2:
            flash("Tus datos son inválidos")
            return redirect("/profile")
        db.session.execute("""UPDATE `usuarios`
        SET
        nombre= :n,
        apellido= :a,
        password= :pw
        WHERE id= :id
        """,
        {
        "n":nombre,
        "a":apellido,
        "pw": passwordEncrypted,
        "id": session["id"]
        })
        db.session.commit()
        session["name"] = nombre
        session["surname"] = apellido
        flash("Has modificado tu usuario")
        return redirect("/profile")

