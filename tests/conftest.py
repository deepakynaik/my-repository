from fastapi.testclient import TestClient
import copy
import pytest
from src.app import app, activities

@pytest.fixture
def client():
    # Arrange: snapshot the in-memory activities
    original = copy.deepcopy(activities)
    client = TestClient(app)
    try:
        # Act: provide a TestClient to the test
        yield client
    finally:
        # Assert/Teardown: restore original activities to ensure isolation
        activities.clear()
        activities.update(original)
