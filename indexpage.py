from head import *
def root():
    @app.route("/")
    def root():
            return "Welcome page"
