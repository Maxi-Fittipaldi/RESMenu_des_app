from flask import Flask, render_template, request, url_for, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def root():
        return "Welcome page"

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        mail = request.form["mail"]
        password = request.form["pwd"]
        return redirect("/profile")
    else:
        return render_template("login.html")
@app.route("/profile")
def profile():
    return "profile"
if __name__ == "__main__":
   app.run(debug=True)
