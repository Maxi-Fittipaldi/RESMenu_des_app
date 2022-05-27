from flask import Flask, render_template, request, url_for, redirect, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
import encrypt
app = Flask(__name__)
db = SQLAlchemy(app)

userPasswordEncrypted = encrypt("Pepe123")

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route("/")
def root():
        return "Welcome page"

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        mail = request.form["mail"]
        password = request.form["pwd"]
        session["mail"] = mail
        passwordEncrypted = encrypt(password)
        if passwordEncrypted.hexdigest() == userPasswordEncrypted.hexdigest():
                return redirect("/profile")
        else:
                return redirect("/login")
    else:
        return render_template("login.html")
@app.route("/profile")
def profile():
    if "mail" in session:
        return f'iniciaste sesión como {session["mail"]}'
    return "no iniciaste sesión"

@app.route("products/select/<int:id>", methods=['GET','POST'])
def search():
    if request.method == "POST":
        productName = request.form["name"]
        db.session.execute("SELECT * FROM products WHERE productName = :n",
                           {"n":productName})
        db.session.commit()
    else:
        return render_template("productos.html")

@app.route("products/select/<int:id>")
def select():
    db.session.execute("SELECT * FROM products")
    db.session.commit()
    return redirect("/")

@app.route("/products/insert/<int:id>", methods=['GET','POST'])
def insert(): 
    if request.method == "POST":
        productName = request.form["name"]
        productPrice = request.form["price"]
        productStock = request.form["quantity_in_stock"]
        db.session.execute("INSERT INTO products (name,price,quantity_in_stock) VALUES(:n,:p ,:s)",
                           {"n":productName,"p":productPrice,"s":productStock})
        db.session.commit()
        return redirect("/")
    else:
        products = db.session.execute("SELECT * FROM products")
        return render_template('index.html',products=products)

@app.route("/delete/<int:id>")
def delete(id):
    db.session.execute("DELETE FROM products WHERE id = :id",{"id":id})
    db.session.commit()
    return redirect("/")
    
@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    if request.method == "POST":
        productName = request.form["name"]
        productPrice = request.form["price"]
        productStock = request.form["quantity_in_stock"]
        db.session.execute("UPDATE products SET name= :n ,price= :p ,quantity_in_stock= :s WHERE id= :id",
                           {"n":productName,"p":productPrice,"s":productStock,"id":id})
        db.session.commit()
        return redirect("/")
if __name__ == "__main__":
   app.run(debug=True)

@app.route('/logout')
def logout():
    session.pop('mail', None)
    return redirect("/login")
if __name__ == "__main__":
   app.run(debug=True)
