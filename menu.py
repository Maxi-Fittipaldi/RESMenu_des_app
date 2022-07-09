from head import *
def menu():
    @app.route("/menu", methods=['GET'])
    def menu():
        productos = db.session.execute("SELECT * FROM productos")
        return render_template("menu.html",productos=productos)
def commit():
    @app.route("/menu/commit",methods=["POST"])
    def commit():
        content_type = request.headers.get("Content-Type")
        json = request.json()
        print(json["product_ids"])
        return redirect("/menu")
