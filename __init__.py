#general config
from flask import Flask
app = Flask(__name__)
app.config.from_pyfile("config.py")
#email
from flask_mail import Mail
mail = Mail(app)
#db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

#blueprints
from . import auth
from . import indexpage
from . import manage
from . import profile
from . import orders
app.register_blueprint(auth.bp)
app.register_blueprint(indexpage.bp)
app.register_blueprint(manage.bp)
app.register_blueprint(profile.bp)
app.register_blueprint(orders.bp)



if __name__ == "__main__":
   app.run()
