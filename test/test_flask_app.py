import unittest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_root_context():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello FastAPI🚀"}


if __name__ == '__main__':
    unittest.main()
