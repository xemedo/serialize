from app import db
from app.models import Product


def test_create_product(app, client, company, product):
    with app.app_context():
        response = product
        assert response.status_code == 200
        assert db.session.query(Product).count() == 1


def test_get_product(app, client, company, product):
    with app.app_context():
        product = db.session.query(Product).first()
        response = client.get("products/{}".format(product.id))
        assert response.status_code == 200


def test_update_product(app, client, company, product):
    with app.app_context():
        product = db.session.query(Product).first()
        response = client.put(
            "products/{}".format(product.id),
            json={"discount": "8€", "price": "1400€"},
        )
        updated_product = db.session.query(Product).filter_by(id=product.id).first()
        assert updated_product.price == "1400€"
        assert response.status_code == 200
