from flask import Flask, render_template, request, url_for, redirect, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
from encrypt import *

app = Flask(__name__)
#mysql
#app.config['SQLALCHEMY_DATABASE_URI']="mysql://testing:12345@127.0.0.1:3306/RESMenu"
#mariadb
app.config['SQLALCHEMY_DATABASE_URI']="mariadb+mariadbconnector://testing:12345@127.0.0.1:3306/RESMenu"
db = SQLAlchemy(app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
userPasswordEncrypted = encrypt("Pepe123")

@app.route("/")
def root():
        products = db.session.execute("SELECT * FROM productos") #sólo de testeo
        return "Welcome page"

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        mail = request.form["mail"]
        password = request.form["pwd"]
        session["mail"] = mail
        passwordEncrypted = encrypt(password)
        if passwordEncrypted == userPasswordEncrypted:
                return redirect("/profile")
        else:
                return redirect("/login")
    else:
        return render_template("login.html")
@app.route("/profile")
def profile():
    if "mail" in session:
        return f'iniciaste sesión como {session["mail"]}'
    return "no iniciaste sesión"

@app.route('/logout')
def logout():
    session.pop('mail', None)
    return redirect("/login")
if __name__ == "__main__":
   app.run(debug=True)
