from flask import Flask, render_template, request, url_for, redirect, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
import encrypt

userPasswordEncrypted = encrypt("Pepe123")

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route("/")
def root():
        return "Welcome page"

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        mail = request.form["mail"]
        password = request.form["pwd"]
        session["mail"] = mail
        passwordEncrypted = encrypt(password)
        if passwordEncrypted.hexdigest() == userPasswordEncrypted.hexdigest():
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
