from flask import Flask, render_template, render_template_string, request, url_for, redirect, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
import encrypt
app = Flask(__name__)
db = SQLAlchemy(app)

@app.route("manage/search", methods=['GET','POST'])
def search():
    if request.method == "POST":
        productoNombre = request.form["nombre"]
        db.session.execute("SELECT * FROM productos WHERE productonombre = :n",
                           {"n":productoNombre})
        db.session.commit()
    else:
        return render_template("productos.html")

@app.route("manage/select")
def select():
    db.session.execute("SELECT * FROM productos")
    db.session.commit()
    return redirect("/")

@app.route("manage/insert/<int:id>", methods=['GET','POST'])
def insert(): 
    if request.method == "POST":
        productoNombre = request.form["nombre"]
        productoPrecio = request.form["precio"]
        productoStock = request.form["cantidad_en_stock"]
        db.session.execute("INSERT INTO productos (nombre,precio,cantidad_en_stck) VALUES(:n,:p ,:s)",
                           {"n":productoNombre,"p":productoPrecio,"s":productoStock})
        db.session.commit()
        return redirect("/")
    else:
        productos = db.session.execute("SELECT * FROM productos")
        return render_template('index.html',productos=productos)

@app.route("manage/delete/<int:id>")
def delete(id):
    if request.method == "POST":
        productoid = request.form["id"]
        db.session.execute("DELETE FROM productos WHERE id = :id",{"id":productoid})
        db.session.commit()
        return redirect("/")
    else:
        productos = db.session.execute("SELECT * FROM productos")
        return render_template('index.html',productos=productos)

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