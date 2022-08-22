from flask import Blueprint, render_template, request, url_for, redirect, send_from_directory, session, flash
from RESMenu_des_app import db
bp = Blueprint('menu', __name__, url_prefix='/')

@bp.route("/menu", methods=['GET'])
def menu():
    productos = db.session.execute("SELECT * FROM productos")
    return render_template("menu.html",productos=productos, session=session)
@bp.route("/menu/commit",methods=["POST"])
def commit():
    content_type = request.headers.get("Content-Type")
    json = request.json
    for x in json["product_ids"]:
        print(x)
    db.session.execute(
        """INSERT INTO 
        cabeceraTransaccion (usuario_id,nro_mesa,estado)
        VALUES(:uid, :nm, :e)""",
    {"uid": session["id"],
    "nm":session["nTable"],
    "e": "pendiente"})
    db.session.execute("""
    
    """)
    session["order?"] = True
    return redirect("/menu")
