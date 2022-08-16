from flask import Blueprint, render_template, request, url_for, redirect, send_from_directory, session, flash
from RESMenu_des_app.encrypt import *
from RESMenu_des_app import db
bp = Blueprint('profile', __name__, url_prefix='/')
@bp.route("/profile")
def profile():
    if "id" in session:
        return render_template("profile.html", session=session)
    return redirect("/login")


@bp.route("/profile/update",  methods=['POST'])
def update():
    if not "id" in session:
        return redirect("/login")
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        password = request.form["password"]
        email = request.form["email"]
        passwordEncrypted = encrypt(password)
        db.session.execute("""UPDATE `usuarios`
        SET gmail= :g,
        nombre= :n,
        apellido= :a,
        password= :pw
        WHERE id= :id
        """,
        {
        "g":email,
        "n":nombre,
        "a":apellido,
        "pw": passwordEncrypted,
        "id": session["id"]
        })
        db.session.commit()
        session["name"] = nombre
        session["surname"] = apellido
        session["email"] = email
        flash("Has modificado tu usuario")
        return redirect("/profile")

