from marshmallow import ValidationError
from flask_restful import Resource
from flask import request

from app.schemas.company import CompanySchema
from app import db

class CompanyCreateView(Resource):
    def post(self):
        product_data = request.get_json(force=True)
        schema = CompanySchema()
        try:
            new_company = schema.load(product_data, session=db.session)
            db.session.add(new_company)
            db.session.commit()
        except ValidationError as err:
            return err.messages, 400

        return str(new_company.id), 200