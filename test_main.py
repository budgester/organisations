from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_organisations():
    response = client.get("/organisations")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_organisation_structure():
    response = client.get("/organisations")
    data = response.json()
    org = data[0]
    assert "id" in org
    assert "name" in org
    assert "description" in org
