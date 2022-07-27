from flask import Flask

app = Flask(__name__)
#db

from flask_sqlalchemy import SQLAlchemy
#mysql
#app.config['SQLALCHEMY_DATABASE_URI']="mysql://testing:12345@127.0.0.1:3306/RESMenu"
#mariadb
app.config['SQLALCHEMY_DATABASE_URI']="mariadb+mariadbconnector://testing:12345@127.0.0.1:3306/RESMenu"
#---
#
db = SQLAlchemy(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#blueprints
from . import auth
from . import indexpage
from . import manage
from . import profile
app.register_blueprint(auth.bp)
app.register_blueprint(indexpage.bp)
app.register_blueprint(manage.bp)
app.register_blueprint(profile.bp)



if __name__ == "__main__":
   app.run(debug=True)
