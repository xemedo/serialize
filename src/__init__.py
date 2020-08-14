from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()

def create_app(testing=False):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    configure_app(app, testing)

    db.init_app(app)
    migrate.init_app(app, db)

    from src.views.product import ProductCreateView, ProductEntityView
    api = Api(app)
    api.add_resource(ProductCreateView, "/products/")
    api.add_resource(ProductEntityView, "/products/<id>/")

    return app

def configure_app(app, testing):
    if testing is None:
        from src.config import Config
        app.config.from_object(Config)

