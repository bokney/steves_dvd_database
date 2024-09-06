import pytest
from main import app
from db.run_seed import seed_db
from fastapi.testclient import TestClient

# @pytest.fixture(scope='function')

@pytest.fixture(autouse=True)
def reset_db():
    
    seed_db()

class TestMain:

    def test_read_root(self):
        test_client = TestClient(app)
        response = test_client.get("/")
        assert response.status_code == 200
        assert response.json() == "server is running ✅"

    def test_create_item(self):
        test_client = TestClient(app)
        response = test_client.post("/items/", json={
            "name": "Escape from the Planet of the Apes",
            "description": "Three apes travel back in time"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Escape from the Planet of the Apes"
        assert data["description"] == "Three apes travel back in time"
        assert "item_id" in data
        