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
            db.session.execute("""INSERT INTO cabeceraTransaccion
            (Usuarioid, Fecha, Estado)
            VALUES(:id, :f, :e)""", 
            {
            "id": session["id"],
            "f":fecha,
            "e":estado, 
            })
            db.session.commit()
            return render_template("menu.html",productos=productos)
        else:
            productos = db.session.execute("SELECT * FROM cabeceraTransaccion")
            return render_template('menu.html',productos=productos)