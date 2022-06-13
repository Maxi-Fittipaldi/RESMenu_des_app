from flask import Flask, render_template, request, url_for, redirect, send_from_directory, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from encrypt import *

app = Flask(__name__)
#mysql
app.config['SQLALCHEMY_DATABASE_URI']="mysql://testing:12345@127.0.0.1:3306/RESMenu"
#mariadb
#app.config['SQLALCHEMY_DATABASE_URI']="mariadb+mariadbconnector://testing:12345@127.0.0.1:3306/RESMenu"
db = SQLAlchemy(app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def root():
        products = db.session.execute("SELECT * FROM productos") #sólo de testeo
        return "Welcome page"

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        mail = request.form["mail"]
        password = request.form["pwd"]
        passwordEncrypted = encrypt(password)
        query = db.session.execute("SELECT password, gmail FROM usuarios WHERE gmail = :mail",{"mail": mail})
        dbGmail = None
        dbPassword = None
        for result in query:
                dbGmail = result["gmail"]
                dbPassword = result["password"]
        if passwordEncrypted != dbPassword or mail != dbGmail:
                flash("La contraseña o el mail son incorrectos")
                return redirect("/login")

        session["mail"] = mail
        flash("Has iniciado sessión")
        return redirect("/profile")
    else:
        return render_template("login.html")
@app.route("/signup", methods = ["GET","POST"])
def signup():
        if request.method == "POST":
               mail = request.form["mail"]
               nombre = request.form["nombre"]
               apellido = request.form["apellido"]
               password = request.form["pwd"]
               passwordEncrypted = encrypt(password)
               query = db.session.execute("SELECT gmail FROM usuarios WHERE gmail = :mail",{"mail": mail})
               dbGmail = None
               for resutl in query:
                       dbGmail = result["gmail"]
               if mail == dbGmail:
                       flash("Esta cuenta ya existe")
                       return redirect("/signup")
               db.session.execute(
                """INSERT INTO usuarios
               (gmail,nombre,apellido,password,estado)
               VALUES(:mail,:nomb,:apel,:pass,'pendiente' )""",
                {"mail": mail,
                 "nomb": nombre,
                 "apel": apellido,
                 "pass": passwordEncrypted})
               db.session.commit()
               flash("usuario registrado")
               return redirect("/login")
        return render_template("signup.html")
@app.route("/profile")
def profile():
    if "mail" in session:
        return render_template("profile.html")
    return "no iniciaste sesión"

@app.route("/manage/search", methods=['GET'])
def search():
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

@app.route("/manage")
def select():
    productos = db.session.execute("SELECT * FROM productos")
    return render_template("manage.html", productos=productos)

@app.route("/manage/insert", methods=['GET','POST'])
def insert(): 
    if request.method == "POST":
        productoNombre = request.form["nombre"]
        productoPrecio = request.form["precio"]
        productoDesc = request.form["descripcion"]
        horariod = request.form["horariod"]
        horarioh = request.form["horarioh"]
        db.session.execute("""INSERT INTO productos 
        (nombre,precio,descripcion, disponibilidad_desde, disponibilidad_hasta, propietario)
        VALUES(:n,:p ,:d, :dd,:dh,2)""",
        {
        "n":productoNombre,
        "p":productoPrecio,
        "d": productoDesc,
        "dd": horariod,
        "dh": horarioh
        })
        db.session.commit()
        return redirect("/manage")
    else:
        productos = db.session.execute("SELECT * FROM productos")
        return render_template('index.html',productos=productos)

@app.route("/manage/delete/<int:id>")
def delete(id):
    productoid = id
    db.session.execute("DELETE FROM productos WHERE id = :id",{"id":productoid})
    db.session.commit()
    return redirect("/manage")

@app.route("/manage/update/<int:id>", methods=["GET","POST"])
def update(id):
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
if __name__ == "__main__":
   app.run(debug=True)

@app.route('/logout')
def logout():
    session.pop('mail', None)
    return redirect("/login")
if __name__ == "__main__":
   app.run(debug=True)
