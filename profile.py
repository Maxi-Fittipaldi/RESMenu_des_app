from flask import Blueprint, render_template, request, url_for, redirect, send_from_directory, session, flash
bp = Blueprint('profile', __name__, url_prefix='/')
@bp.route("/profile")
def profile():
    if "id" in session:
        return render_template("profile.html", session=session)
    return redirect("/login")


@bp.route("/profile/update")
def update():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        password = request.form["password"]
        gmail = request.form["gmail"]
        db.session.execute("""UPDATE `usuarios`
        SET gmail= :g,
        nombre= :n,
        apellido= :a,
        password= :pw
        WHERE id= :id
        """,
        {
        "g":gmail,
        "n":nombre,
        "a":apellido,
        "pw":password,
        "id":id
        })
        db.session.commit()
        return redirect("/profile")

