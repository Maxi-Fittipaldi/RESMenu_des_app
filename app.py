from flask import Flask, render_template, request, url_for, redirect, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
import encrypt
app = Flask(__name__)
db = SQLAlchemy(app)

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

@app.route("manage/search", methods=['GET','POST'])
def search():
    if request.method == "POST":
        productoNombre = request.form["nombre"]
        db.session.execute("SELECT * FROM productos WHERE productonombre = :n",
                           {"n":productoNombre})
        return redirect("manage/search")
    else:
        return render_template("buscar.html")

@app.route("/manage")
def select():
    productos = db.session.execute("SELECT * FROM productos")
    return render_template("manage.html", productos=productos)

@app.route("manage/insert/<int:id>", methods=['GET','POST'])
def insert(): 
    if request.method == "POST":
        productoNombre = request.form["nombre"]
        productoPrecio = request.form["precio"]
        productoStock = request.form["cantidad_en_stock"]
        db.session.execute("INSERT INTO productos (nombre,precio,cantidad_en_stck) VALUES(:n,:p ,:s)",
                           {"n":productoNombre,"p":productoPrecio,"s":productoStock})
        db.session.commit()
        return redirect("/manage")
    else:
        productos = db.session.execute("SELECT * FROM productos")
        return render_template('index.html',productos=productos)

@app.route("manage/delete/<int:id>")
def delete(id):
    productoid = id
    db.session.execute("DELETE FROM productos WHERE id = :id",{"id":productoid})
    db.session.commit()
    return redirect("/manage")

@app.route("manage/update/<int:id>", methods=["GET","POST"])
def update(id):
    if request.method == "POST":
        productoNombre = request.form["nombre"]
        productoPrecio = request.form["precio"]
        productoStock = request.form["cantidad_en_stock"]
        db.session.execute("UPDATE productos SET nombre= :n ,precio= :p ,cantidad_en_stock= :s WHERE id= :id",
                           {"n":productoNombre,"p":productoPrecio,"s":productoStock,"id":id})
        db.session.commit()
        return redirect("/")
if __name__ == "__main__":
   app.run(debug=True)

@app.route('/logout')
def logout():
    session.pop('mail', None)
    return redirect("/login")
if __name__ == "__main__":
   app.run(debug=True)
