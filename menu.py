from head import *
def buy():
    @app.route("/menu/buy/<int:id>", methods=['GET'])
    def buy(id):
        productoid = id
        
        return redirect("/menu")
