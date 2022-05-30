from flask import Flask, render_template, request, url_for, redirect, send_from_directory, session, flash
from flask_sqlalchemy import SQLAlchemy
from encrypt import *

app = Flask(__name__)
#mysql
#app.config['SQLALCHEMY_DATABASE_URI']="mysql://testing:12345@127.0.0.1:3306/RESMenu"
#mariadb
app.config['SQLALCHEMY_DATABASE_URI']="mariadb+mariadbconnector://testing:12345@127.0.0.1:3306/RESMenu"
db = SQLAlchemy(app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def root():
        products = db.session.execute("SELECT * FROM productos") #sólo de testeo
        return "Welcome page"

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        mail = request.form["mail"]
        password = request.form["pwd"]
        passwordEncrypted = encrypt(password)
        query = db.session.execute("SELECT password, gmail FROM usuarios WHERE gmail = :mail",{"mail": mail})
        dbGmail = None
        dbPassword = None
        for result in query:
                dbGmail = result["gmail"]
                dbPassword = result["password"]
        if passwordEncrypted != dbPassword or mail != dbGmail:
                flash("La contraseña o el mail son incorrectos")
                return redirect("/login")

        session["mail"] = mail
        flash("Has iniciado sessión")
        return redirect("/profile")
    else:
        return render_template("login.html")
@app.route("/signup", methods = ["GET","POST"])
def signup():
        return render_template("signup.html")
@app.route("/profile")
def profile():
    if "mail" in session:
        return render_template("profile.html")
    return "no iniciaste sesión"

@app.route('/logout')
def logout():
    session.pop('mail', None)
    return redirect("/login")
if __name__ == "__main__":
   app.run(debug=True)
