from flask import Blueprint, render_template, request, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from RESMenu_des_app.misc.encrypt import *
from RESMenu_des_app import db
from RESMenu_des_app.token import *
from .login import *
from RESMenu_des_app.mail import send_email
from datetime import datetime
from random import random
bp = Blueprint('auth', __name__, url_prefix='/')
@bp.route("/login", methods = ["GET","POST"])
def login():
    if "cid" in session:
        return redirect(url_for("menu.menu"))
    client_id = encrypt(str(datetime.now()) + str(random()))
    session["cid"] = client_id
    session["client"] = True
    session["order?"] = False
    return redirect(url_for("menu.menu"))

@bp.route("/staff/login", methods = ["GET","POST"])
def staff_login():
    if "id" in session:
        return redirect("/profile")
    if request.method == "POST":
        email = request.form["mail"]
        password = request.form["pwd"]
        passwordEncrypted = encrypt(password)
        query = db.session.execute("SELECT * FROM usuarios WHERE email = :email",{"email": email})
        dbEmail = None
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
            dbEmail = result["email"]
            dbPassword = result["password"]
            dbState = result["estado"]
            dbRol = result["rol"]
        if passwordEncrypted != dbPassword or email != dbEmail:
            flash("La contraseña o el mail son incorrectos", "warning")
            return redirect(url_for("auth.staff_login"))
        session["id"] = dbId
        session["name"] = dbName
        session["surname"] = dbSurname
        session["email"] = dbEmail
        session["state"] = dbState
        session["rol"] = dbRol
        flash("Has iniciado sessión","success")
        return redirect("/profile")
    return render_template("staff_login.html")
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
            query = db.session.execute("SELECT email FROM usuarios WHERE email = :email",{"email": email})
            dbEmail = None
            for result in query:
                    dbEmail = result["email"]
            if email == dbEmail:
                    flash("Esta cuenta ya existe", "warning")
                    return redirect("/signup")
            db.session.execute(
                """INSERT INTO usuarios
            (email,nombre,apellido,password,estado)
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
            flash("Usuario registrado, verifique la cuenta.", "success")
            session["rol"] = "sin_rol"
            return redirect(url_for("auth.staff_login"))
        return render_template("signup.html")

@bp.route("/confirm/<token>")
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('El código ha expirado o es incorrecto, intenta iniciar sesión y reenviarlo', 'warning')
        return redirect(url_for("auth.staff_login"))
    user = db.session.execute('SELECT * FROM usuarios WHERE email = :email', {'email': email})
    userStatus = None
    for result in user:
        userStatus = result["estado"]
        userEmail = result["email"]
    if userEmail != email:
        if "id" in session:
            flash('El código ha expirado o es incorrecto, intenta reenviarlo.', 'warning')
            return redirect("/profile")
        else:
            flash('El código ha expirado o es incorrecto, intenta iniciar sesión y reenviarlo.', 'warning')
            return redirect(url_for("auth.staff_login"))
    if userStatus == 'verificado':
        flash('La cuenta ha sido verificada previamente. Por favor, inicie sesión.')
    else:
        db.session.execute("UPDATE usuarios SET estado = 'verificado' WHERE email = :email ", {'email': email})
        db.session.commit()
        flash('Has verificado la cuenta, gracias.', 'success')
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
    session.pop("rol",None)
    return redirect(url_for("auth.staff_login"))
