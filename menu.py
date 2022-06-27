from head import *
def menu():
    @app.route("/menu", methods=['GET'])
    def menu():
        if not "id" in session:
            return redirect("/login")
        productos = db.session.execute("SELECT * FROM productos")
        return render_template("menu.html",productos=productos)
def menu_commit():
    @app.route("/menu/commit", methods=['POST'])
    def menu_commit():
        if not "id" in session:
            return redirect("/login")
        if request.method=="POST": 
            productoid=request.form["Productoid"]
            Monto=request.form["Precio"]
            Cantidad=request.form["Cantidad"]
            
        db.session.execute("""INSERT INTO productos
                (Productoid, Cantidad, Monto)
                VALUES(:n,:p ,:c)""",
                {
                "n":productoNombre,
                "p":productoPrecio,
                "c":productocantidad,
                })
        db.session.commit()
        return render_template("menu.html",productos=productos)



