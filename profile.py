from head import *

def profile():
    @app.route("/profile")
    def profile():
        if not "id" in session:
            return redirect("/login")
        return render_template("profile.html")
