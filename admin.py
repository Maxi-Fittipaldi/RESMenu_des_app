from flask import(Blueprint,
render_template, request, url_for, redirect,
send_from_directory, session, flash)
from RESMenu_des_app import db
from .login import admin_required, staff_login_required
from .misc.encrypt import encrypt
bp = Blueprint('admin',__name__, url_prefix='/admin')

@bp.route("/",methods=["GET"])
@staff_login_required
@admin_required
def select():
    usuarios = db.session.execute("SELECT * FROM usuarios")
    return render_template("admin.html", usuarios=usuarios)

@bp.route("/insert", methods=['POST'])
@staff_login_required
@admin_required
def insert():
        usuarioNombre = request.form["nombre"]
        usuarioApellido = request.form["apellido"]
        usuarioPassword = encrypt(request.form["pwd"])
        usuarioRol = request.form["rol"]
        usuarioEstado = request.form["estado"]
        usuarioEmail = request.form["email"]
        try:
                db.session.execute("""INSERT INTO usuarios
                (nombre, apellido, password, rol, estado, email)
                VALUES(:n,:a , :p, :r, :e, :em)""",
                {
                "n": usuarioNombre,
                "a": usuarioApellido,
                "p": usuarioPassword,
                "r": usuarioRol,
                "e": usuarioEstado,
                "em": usuarioEmail
                })
                db.session.commit()
        except Exception as e:
                print(e)
                flash("Ocurrió un error en la inserción", "error")
        return redirect(url_for("admin.select"))

@bp.route("/delete/<int:id>")
@staff_login_required
@admin_required
def delete(id):
    if id == 1:
        flash("No puedes borrarte a tí mismo", "error")
        return redirect(url_for("admin.select"))
    db.session.execute("DELETE FROM usuarios WHERE id = :id",{"id":id})
    db.session.commit()
    return redirect(url_for("admin.select"))


@bp.route("/update/<int:id>", methods=["POST"])
@staff_login_required
@admin_required
def update(id):
        usuarioNombre = request.form["nombre"]
        usuarioApellido = request.form["apellido"]
        usuarioEmail = request.form["email"]
        usuarioRol = request.form["rol"]
        usuarioEstado = request.form["estado"]
        if id == 1 and usuarioRol != "admin" or usuarioEstado != "verificado":
            flash("No puedes descender de privilegios", "error")
            return redirect(url_for("admin.select"))
        db.session.execute("""UPDATE usuarios
        SET nombre= :n ,
        apellido = :a,
        rol = :r,
        estado = :e,
        email = :em
        WHERE id= :id
        """,
        {
        "n": usuarioNombre,
        "a": usuarioApellido,
        "r": usuarioRol,
        "e": usuarioEstado,
        "em": usuarioEmail,
        "id":id
        })
        db.session.commit()
        return redirect(url_for("admin.select"))
