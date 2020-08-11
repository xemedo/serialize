from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from src.models.product import Product
from src.utils import FilteredSchema

class ProductSchema(SQLAlchemyAutoSchema, FilteredSchema):
    class Meta:
        model = Product
        load_instance = True
        include_fk = True

    discount = auto_field(load_only=True)