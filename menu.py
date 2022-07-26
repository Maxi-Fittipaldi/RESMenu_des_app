from flask import Blueprint, render_template, request, url_for, redirect, send_from_directory, session, flash
from RESMenu_des_app import db
bp = Blueprint('menu', __name__, url_prefix='/')

@bp.route("/menu", methods=['GET'])
def menu():
    productos = db.session.execute("SELECT * FROM productos")
    return render_template("menu.html",productos=productos)
@bp.route("/menu/commit",methods=["POST"])
def commit():
    content_type = request.headers.get("Content-Type")
    json = request.json
    for x in json["product_ids"]:
        print(x)
    return redirect("/menu")
