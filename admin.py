from flask import(Blueprint,
render_template, request, url_for, redirect,
send_from_directory, session, flash)
from RESMenu_des_app import db
from .login import admin_required, staff_login_required
bp = Blueprint('admin',__name__, url_prefix='/admin')

@bp.route("/",methods=["GET"])
@staff_login_required
@admin_required
def select():
    usuarios = db.session.execute("SELECT * usuarios")
    return render_template("admin.html", usuarios=usuarios) 