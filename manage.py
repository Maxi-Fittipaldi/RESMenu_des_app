from flask import Flask, render_template, render_template_string, request, url_for, redirect, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
import encrypt
app = Flask(__name__)
db = SQLAlchemy(app)

@app.route("manage/search", methods=['GET','POST'])
def search():
    if request.method == "POST":
        productName = request.form["name"]
        db.session.execute("SELECT * FROM products WHERE productName = :n",
                           {"n":productName})
        db.session.commit()
    else:
        return render_template("productos.html")

@app.route("manage/select")
def select():
    db.session.execute("SELECT * FROM products")
    db.session.commit()
    return redirect("/")

@app.route("manage/insert>", methods=['GET','POST'])
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

@app.route("manage/delete/<int:id>")
def delete(id):
    if request.method == "POST":
        productid = request.form["id"]
        db.session.execute("DELETE FROM products WHERE id = :id",{"id":productid})
        db.session.commit()
        return redirect("/")
    else:
        products = db.session.execute("SELECT * FROM products")
        return render_template('index.html',products=products)

@app.route("manage/update/<int:id>", methods=["GET","POST"])
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