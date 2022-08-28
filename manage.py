#!/usr/bin/env python3

from flask import(Blueprint,
render_template, request, url_for, redirect,
send_from_directory, session, flash)
from RESMenu_des_app import db
bp = Blueprint('manage',__name__, url_prefix='/')
@bp.route("/manage/search", methods=['GET'])
def search():
        if not "id" in session:
            return redirect("/login")
        if session["rol"] == "cliente":
            return redirect("/profile")
        if session["state"] == "pendiente":
            return redirect("/profile")
        productoNombre = request.args.get("nombre",None)
        productosRaw = db.session.execute("SELECT * FROM productos WHERE nombre = :n",
                        {"n":productoNombre})
        productos = []
        for x in productosRaw:
                productos.append(x)
        if len(productos) == 0:
                flash("Tu consulta no ha retornado resultados")
                return redirect("/manage")
        return render_template("search_results.html", productos=productos)
@bp.route("/manage")
def select():
    if not "id" in session:
        return redirect("/login")
    if session["rol"] == "cliente":
        return redirect("/profile")
    if session["state"] == "pendiente":
        return redirect("/profile")
    productos = db.session.execute("SELECT * FROM productos")
    return render_template("manage.html", productos=productos)

@bp.route("/manage/insert", methods=['GET','POST'])
def insert():
    if not "id" in session:
        return redirect("/login")
    if session["rol"] == "cliente":
        return redirect("/profile")
    if session["state"] == "pendiente":
        return redirect("/profile")
    if request.method == "POST":
        productoNombre = request.form["nombre"]
        productoPrecio = request.form["precio"]
        productoDesc = request.form["descripcion"]
        horariod = request.form["horariod"]
        horarioh = request.form["horarioh"]
        db.session.execute("""INSERT INTO productos
        (nombre,precio,descripcion, disponibilidad_desde, disponibilidad_hasta, propietario)
        VALUES(:n,:p ,:d, :dd,:dh,:prop)""",
        {
        "n":productoNombre,
        "p":productoPrecio,
        "d": productoDesc,
        "dd": horariod,
        "dh": horarioh,
        "prop": session["id"]
        })
        db.session.commit()
        return redirect("/manage")
    else:
        productos = db.session.execute("SELECT * FROM productos")
        return render_template('index.html',productos=productos)
@bp.route("/manage/delete/<int:id>")
def delete(id):
    if not "id" in session:
        return redirect("/login")
    if session["rol"] == "cliente":
        return redirect("/profile")
    if session["state"] == "pendiente":
        return redirect("/profile")
    productoid = id
    db.session.execute("DELETE FROM productos WHERE id = :id",{"id":productoid})
    db.session.commit()
    return redirect("/manage")
@bp.route("/manage/update/<int:id>", methods=["GET","POST"])
def update(id):
    if not "id" in session:
        return redirect("/login")
    if session["rol"] == "cliente":
        return redirect("/profile")
    if session["state"] == "pendiente":
        return redirect("/profile")
    if request.method == "POST":
        productoNombre = request.form["nombre"]
        productoPrecio = request.form["precio"]
        productoDesc = request.form["descripcion"]
        horariod = request.form["horariod"]
        horarioh = request.form["horarioh"]
        db.session.execute("""UPDATE productos
        SET nombre= :n ,
        precio= :p,
        descripcion = :d,
        disponibilidad_desde = :dd,
        disponibilidad_hasta = :dh
        WHERE id= :id
        """,
        {
        "n":productoNombre,
        "p":productoPrecio,
        "d": productoDesc,
        "dd": horariod,
        "dh": horarioh,
        "id":id
        })
        db.session.commit()
        return redirect("/manage")
