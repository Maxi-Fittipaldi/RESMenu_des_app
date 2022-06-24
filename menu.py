from head import *
def menu():
    @app.route("/menu", methods=['GET'])
    def menu():
        productos = db.session.execute("SELECT * FROM productos")
        return render_template("menu.html",productos=productos)
