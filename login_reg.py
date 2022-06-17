#!/usr/bin/env python3
from head import *
from encrypt import *

def login():
    @app.route("/login", methods = ["GET","POST"])
    def login():
        if request.method == "POST":
            mail = request.form["mail"]
            password = request.form["pwd"]
            passwordEncrypted = encrypt(password)
            query = db.session.execute("SELECT id,nombre, apellido, password, gmail FROM usuarios WHERE gmail = :mail",{"mail": mail})
            dbGmail = None
            dbPassword = None
            dbId= None
            dbName= None
            dbSurname= None
            for result in query:
                    dbId = result["id"]
                    dbGmail = result["gmail"]
                    dbPassword = result["password"]
            if passwordEncrypted != dbPassword or mail != dbGmail:
                    flash("La contraseña o el mail son incorrectos")
                    return redirect("/login")

            session["id"] = dbId
            session["nombre"] = dbName
            session["apellido"] = dbSurname
            session["mail"] = dbGmail
            flash("Has iniciado sessión")
            return redirect("/profile")
        else:
            return render_template("login.html")
def signup():
    @app.route("/signup", methods = ["GET","POST"])
    def signup():
            if request.method == "POST":
                mail = request.form["mail"]
                nombre = request.form["nombre"]
                apellido = request.form["apellido"]
                password = request.form["pwd"]
                passwordEncrypted = encrypt(password)
                query = db.session.execute("SELECT gmail FROM usuarios WHERE gmail = :mail",{"mail": mail})
                dbGmail = None
                for resutl in query:
                        dbGmail = result["gmail"]
                if mail == dbGmail:
                        flash("Esta cuenta ya existe")
                        return redirect("/signup")
                db.session.execute(
                    """INSERT INTO usuarios
                (gmail,nombre,apellido,password,estado)
                VALUES(:mail,:nomb,:apel,:pass,'pendiente' )""",
                    {"mail": mail,
                    "nomb": nombre,
                    "apel": apellido,
                    "pass": passwordEncrypted})
                db.session.commit()
                flash("usuario registrado")
                return redirect("/login")
            return render_template("signup.html")
def logout():
    @app.route('/logout')
    def logout():
        session.pop("id",None)
        session.pop("nombre",None)
        session.pop("apellido",None)
        session.pop("mail",None)
        return redirect("/login")
