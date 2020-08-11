from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None, config_params=None):
    if config_params is None:
        config_params = {}
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    configure_app(app, config, config_params)

    db.init_app(app)
    migrate.init_app(app, db)

    from src.views.product import ProductCreateView, ProductEntityView
    api = Api(app, prefix="/api/v1/")
    api.add_resource(ProductCreateView, "/products/")
    api.add_resource(ProductEntityView, "/products/<id>/")

    return app

def configure_app(app, config, config_params):  # pragma: no cover
    if config is not None:
        from src.config import Config
        app.config.from_object(Config)

    app.config.from_mapping(**config_params)

if __name__ == "__main__":
    application = create_app()
    application.debug = True
    application.run()