from head import *

def profile():
    @app.route("/profile")
    def profile():
        if "mail" in session:
            return render_template("profile.html")
        return "no iniciaste sesión"
