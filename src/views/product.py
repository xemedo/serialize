from marshmallow import ValidationError
from flask_restful import Resource
from flask import (
    request
)

from src.schemas.product import ProductSchema
from main import db
from src.models.product import Product

class ProductCreateView(Resource):
    def post(self):
        product_data = request.get_json(force=True)
        schema = ProductSchema()
        try:
            new_product = schema.load(product_data, session=db.session)
            db.session.add(new_product)
            db.session.commit()
        except ValidationError as err:
            return err.messages, 400

        return 200

class ProductEntityView(Resource):
    def get(self, id):
        product = db.session.query(Product).filter_by(id=id).first()
        schema = ProductSchema(many=False)
        return schema.dump(product), 200

    def put(self, id):
        product = db.session.query(Product).filter_by(id=id).first()
        product_data = request.get_json(force=True)
        try:
            schema = ProductSchema()
            schema.load(
                product_data, instance=product, session=db.session, partial=True
            )
        except ValidationError as err:
            return err.messages, 400
        return 200
