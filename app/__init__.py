from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
db = SQLAlchemy()

def create_app(testing=False):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    configure_app(app, testing)
    init_db(app)

    from app.views.product import ProductCreateView, ProductEntityView
    from app.views.company import CompanyCreateView
    api = Api(app)
    api.add_resource(CompanyCreateView, "/companies")
    api.add_resource(ProductCreateView, "/products")
    api.add_resource(ProductEntityView, "/products/<id>")

    return app

def configure_app(app, testing):
    if not testing:
        from app.config import Config
        app.config.from_object(Config)

def init_db(app):
    from app.models import Company, Product
    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()

