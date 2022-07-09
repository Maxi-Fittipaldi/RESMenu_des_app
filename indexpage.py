from flask import Blueprint, render_template, request, url_for, redirect, send_from_directory, session, flash
bp = Blueprint('indexpage', __name__, url_prefix='/')
@bp.route("/")
def root():
        return "Welcome page"
