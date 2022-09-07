#!/usr/bin/env python3
from flask import session, redirect
from functools import wraps
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not "id" in session:
            return redirect("/login")
        return func(*args, **kwargs)
    return wrapper
def verif_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session["state"] == "pendiente":
            return redirect("/profile")
        return func(*args, **kwargs)
    return wrapper
def staff_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session["rol"] == "cliente":
            return redirect("/profile")
        return func(*args,**kwargs)
    return wrapper
def admin_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session["rol"] != "admin":
            return redirect("/profile")
        return func(*args,**kwargs)
    return wrapper
