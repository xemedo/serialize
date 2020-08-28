from app import db
from app.models.company import Company

def test_create_product(app, client):
    with app.app_context():
        response = client.post("/companies", json={'company_name': "Cool AG"})
        assert response.status_code == 200
        assert db.session.query(Company).count == 1