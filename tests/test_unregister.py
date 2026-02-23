def test_unregister_success_removes_participant(client):
    # Arrange
    email = "michael@mergington.edu"
    activities = client.get("/activities").json()
    assert email in activities["Chess Club"]["participants"]
    # Act
    r = client.delete("/activities/Chess%20Club/signup", params={"email": email})
    # Assert
    assert r.status_code == 200
    activities = client.get("/activities").json()
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_not_signed_up_returns_400(client):
    # Arrange
    email = "not-signed-up@example.com"
    # Act
    r = client.delete("/activities/Chess%20Club/signup", params={"email": email})
    # Assert
    assert r.status_code == 400
    assert r.json().get("detail") == "Student is not signed up for this activity"


def test_unregister_activity_not_found_returns_404(client):
    # Arrange
    email = "someone@example.com"
    # Act
    r = client.delete("/activities/NonExistent/signup", params={"email": email})
    # Assert
    assert r.status_code == 404
    assert r.json().get("detail") == "Activity not found"
