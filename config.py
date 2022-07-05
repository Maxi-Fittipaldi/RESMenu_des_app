class BaseConfig(object):
    """Base configuration."""

    # main config
    SECRET_KEY = 'llave'
    SECURITY_PASSWORD_SALT = 'llave_dos'
    SQLALCHEMY_DATABASE_URI = "mariadb+mariadbconnector://testing:12345@127.0.0.1:3306/RESMenu"
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # mail settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']

    # mail accounts
    MAIL_DEFAULT_SENDER = 'from@example.com'