#!/usr/bin/env python3
from flask import session, redirect, flash
from functools import wraps
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not "id" in session:
            flash("Debes iniciar sesión")
            return redirect("/login")
        return func(*args, **kwargs)
    return wrapper
def verif_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session["state"] == "pendiente":
            flash("Debes tener la cuenta verificada")
            return redirect("/profile")
        return func(*args, **kwargs)
    return wrapper
def staff_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session["rol"] == "cliente":
            flash("No tienes los permisos necesarios")
            return redirect("/profile")
        return func(*args,**kwargs)
    return wrapper
def admin_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session["rol"] != "admin":
            flash("No tienes los permisos necesarios")
            return redirect("/profile")
        return func(*args,**kwargs)
    return wrapper