from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


@pytest.fixture
def mock_mongo_factory():
    mock_factory = MagicMock()
    mock_collection = MagicMock()

    mock_data = [
        {
            "id": 1,
            "description": "A coding resource",
            "url": "https://example.com",
            "types": ["tutorial"],
            "topics": ["web development"],
            "levels": ["beginner"]
        }
    ]

    mock_cursor = MagicMock()
    mock_cursor.skip.return_value = mock_cursor
    mock_cursor.limit.return_value = mock_data
    mock_collection.find.return_value = mock_cursor

    mock_factory.get.return_value = mock_collection
    return mock_factory


def test_get_resources(mock_mongo_factory, monkeypatch):
    monkeypatch.setattr("main.mongo_factory", mock_mongo_factory)

    response = client.get("/resources")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["description"] == "A coding resource"

    response = client.get("/resources", params={"types": ["tutorial"]})
    assert response.status_code == 200
