from flask import Flask, render_template, request, url_for, redirect, send_from_directory, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#mysql
#app.config['SQLALCHEMY_DATABASE_URI']="mysql://testing:12345@127.0.0.1:3306/RESMenu"
#mariadb
db = SQLAlchemy(app)



if __name__ == "__main__":
   app.run(debug=True)
