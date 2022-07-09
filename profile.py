from flask import Blueprint, render_template, request, url_for, redirect, send_from_directory, session, flash
bp = Blueprint('profile', __name__, url_prefix='/')
@bp.route("/profile")
def profile():
    if "id" in session:
        return render_template("profile.html")
    return "no iniciaste sesión"
