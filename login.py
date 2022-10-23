#!/usr/bin/env python3
from flask import session, redirect, flash, url_for
from functools import wraps
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not "id" in session:
            flash("Debes iniciar sesión")
            return redirect(url_for("auth.login"))
        return func(*args, **kwargs)
    return wrapper
def client_only(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session["rol"] != "cliente":
            flash("Área sólo para clientes")
            return redirect(url_for("profile.profile"))
        return func(*args, **kwargs)
    return wrapper
def staff_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session["rol"] == "cliente":
            flash("No tienes los permisos necesarios")
            return redirect(url_for("menu.menu"))
        return func(*args,**kwargs)
    return wrapper
def verif_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session["state"] == "pendiente":
            flash("Debes tener la cuenta verificada")
            return redirect(url_for("profile.profile"))
        return func(*args, **kwargs)
    return wrapper
def chef_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session["rol"] != "chef":
            flash("No tienes los permisos necesarios")
            return redirect(url_for("profile.profile"))
        return func(*args,**kwargs)
    return wrapper
def cashier_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session["rol"] != "cajero":
            flash("No tienes los permisos necesarios")
            return redirect(url_for("profile.profile"))
        return func(*args,**kwargs)
    return wrapper
def admin_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session["rol"] != "admin":
            flash("No tienes los permisos necesarios")
            return redirect(url_for("profile.profile"))
        return func(*args,**kwargs)
    return wrapper
