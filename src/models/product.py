from sqlalchemy_utils import UUIDType
import uuid
from src.utils import CreatedModifiedMixin
from main import db


class Company(db.Model, CreatedModifiedMixin):
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    company_name = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return "<Company {} ({})".format(self.id, self.company_name)


class Product(db.Model, CreatedModifiedMixin):
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False, unique=True)
    price = db.Column(db.String(255), nullable=False, unique=True)
    discount = db.Column(db.String(255), nullable=False, unique=True)

    # relationships
    company_id = db.Column(
        UUIDType(binary=False), db.ForeignKey("company.id"), nullable=False
    )
    company = db.relationship("Company", backref=db.backref("products", lazy=True))

    def __repr__(self):
        return "<Product {} ({})".format(self.id, self.name)
