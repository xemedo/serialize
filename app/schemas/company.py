from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from app.models import Company
from app.utils import FilteredSchema


class CompanySchema(SQLAlchemyAutoSchema, FilteredSchema):
    class Meta:
        model = Company
        load_instance = True
        include_fk = True