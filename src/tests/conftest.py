import pytest
from main import create_app, db
from src.models.product import Company


@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def company(client):
    with client.application.app_context():
        company = Company(company_name="A Company")
        db.session.add(company)
        db.session.commit()
        return company.id


@pytest.fixture
def product(client, company):
    return client.post(
        "/api/v1/products/",
        json={
            "name": "Computer",
            "description": "A highend computer",
            "price": "1200€",
            "company_id": company,
            "discount": "10€",
        },
    )
