from flask import Blueprint, render_template, request, url_for, redirect, send_from_directory, session, flash
from flask_sqlalchemy import SQLAlchemy
from RESMenu_des_app.encrypt import *
from RESMenu_des_app import db
from RESMenu_des_app.token import *
from RESMenu_des_app.mail import send_email
from .login import login_required
bp = Blueprint('auth', __name__, url_prefix='/')
@bp.route("/login", methods = ["GET","POST"])
def login():
    if "id" in session:
        return redirect("/profile")
    if request.method == "POST":
        email = request.form["mail"]
        password = request.form["pwd"]
        nTable = request.form["nTable"]
        passwordEncrypted = encrypt(password)
        query = db.session.execute("SELECT * FROM usuarios WHERE gmail = :email",{"email": email})
        dbGmail = None
        dbPassword = None
        dbId = None
        dbName = None
        dbSurname = None
        dbState = None
        dbRol = None
        for result in query:
                dbId = result["id"]
                dbName = result["nombre"]
                dbSurname = result["apellido"]
                dbGmail = result["gmail"]
                dbPassword = result["password"]
                dbState = result["estado"]
                dbRol = result["rol"]
        if passwordEncrypted != dbPassword or email != dbGmail:
                flash("La contraseña o el mail son incorrectos")
                return redirect("/login")
        pendingOrder = db.session.execute("""SELECT * FROM cabeceraTransaccion
        WHERE usuario_id = :uid AND estado = "pendiente" LIMIT 1""",{"uid": dbId}).scalar()
        if pendingOrder == None:
            session["order?"] = False
        else:
            session["order?"] = True
        session["id"] = dbId
        session["name"] = dbName
        session["surname"] = dbSurname
        session["email"] = dbGmail
        session["state"] = dbState
        session["nTable"] = nTable
        session["rol"] = dbRol
        flash("Has iniciado sessión")
        return redirect("/profile")
    else:
        return render_template("login.html")
@bp.route("/signup", methods = ["GET","POST"])
def signup():
        if "id" in session:
            return redirect("/profile")
        if request.method == "POST":
            email = request.form["mail"]
            nombre = request.form["nombre"]
            apellido = request.form["apellido"]
            password = request.form["pwd"]
            passwordEncrypted = encrypt(password)
            query = db.session.execute("SELECT gmail FROM usuarios WHERE gmail = :email",{"email": email})
            dbGmail = None
            for result in query:
                    dbGmail = result["gmail"]
            if email == dbGmail:
                    flash("Esta cuenta ya existe")
                    return redirect("/signup")
            db.session.execute(
                """INSERT INTO usuarios
            (gmail,nombre,apellido,password,estado)
            VALUES(:email,:nomb,:apel,:pass,'pendiente' )""",
                {"email": email,
                "nomb": nombre,
                "apel": apellido,
                "pass": passwordEncrypted})
            db.session.commit()
            token = generate_confirmation_token(email)
            confirm_url = url_for("auth.confirm_email", token=token, _external=True)
            html = render_template("mail.html", confirm_url=confirm_url)
            subject = "Confirmación de email RESMenu"
            send_email(email, subject, html)
            flash("Usuario registrado, verifique la cuenta.")
            return redirect("/login")
        return render_template("signup.html")

@bp.route("/confirm/<token>")
@login_required
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('El código ha expirado o es incorrecto, intenta iniciar sesión y reenviarlo', 'warning')
        return redirect("/profile")
    user = db.session.execute('SELECT * FROM usuarios WHERE gmail = :email', {'email': email})
    userStatus = None
    for result in user:
        userStatus = result["estado"]
        userEmail = result["gmail"]
    if userEmail != email:
        if "id" in session:
            flash('El código ha expirado o es incorrecto, intenta reenviarlo.', 'warning')
        else:
            flash('El código ha expirado o es incorrecto, intenta iniciar sesión y reenviarlo.', 'warning')
        return redirect("/profile")
    if userStatus == 'verificado':
        flash('La cuenta ha sido verificada previamente. Por favor, inicie sesión.', 'info')
    else:
        db.session.execute("UPDATE usuarios SET estado = 'verificado' WHERE gmail = :email ", {'email': email})
        db.session.commit()
        flash('Has verificado la cuenta, gracias.', 'info')
    return redirect("/logout")
@bp.route("/resend")
def resend():
    email = session["email"]
    token = generate_confirmation_token(email)
    confirm_url = url_for("auth.confirm_email", token=token, _external=True)
    html = render_template("mail.html", confirm_url=confirm_url)
    subject = "Confirmación de email RESMenu (reenviado)"
    send_email(email, subject, html)
    return redirect("/profile")
@bp.route("/logout")
def logout():
    session.pop("id",None)
    session.pop("name",None)
    session.pop("surname",None)
    session.pop("email",None)
    session.pop("state",None)
    session.pop("nTable",None)
    session.pop("order?",None)
    return redirect("/login")
