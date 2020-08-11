import os


class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = "dev-key"
    SECURITY_PASSWORD_SALT = "security-password-salt"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    ENV = "development"
    SERVER_NAME = "127.0.0.1:5000"
    AUTH_TOKEN = "1234"
    WTF_CSRF_ENABLED = True