import os
# main config
SECRET_KEY = '_5#y2L"F4Q8z\n\xec]/'
SECURITY_PASSWORD_SALT = '3%h#3h74fas@@sdHHAS-'
#SQLALCHEMY_DATABASE_URI = "mariadb+mariadbconnector://testing:12345@127.0.0.1:3306/RESMenu"
SQLALCHEMY_DATABASE_URI = "mysql://testing:12345@127.0.0.1:3306/RESMenu"
SQLALCHEMY_TRACK_MODIFICATIONS = False
BCRYPT_LOG_ROUNDS = 13
WTF_CSRF_ENABLED = True
DEBUG_TB_ENABLED = False
DEBUG_TB_INTERCEPT_REDIRECTS = False

# mail settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True

# gmail authentication
MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']

# mail accounts
MAIL_DEFAULT_SENDER = 'from@example.com'
