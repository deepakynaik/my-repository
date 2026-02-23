def test_signup_success_adds_participant(client):
    # Arrange
    email = "tester1@example.com"
    activities = client.get("/activities").json()
    assert email not in activities["Chess Club"]["participants"]
    # Act
    r = client.post("/activities/Chess%20Club/signup", params={"email": email})
    # Assert
    assert r.status_code == 200
    activities = client.get("/activities").json()
    assert email in activities["Chess Club"]["participants"]


def test_signup_activity_not_found_returns_404(client):
    # Arrange
    email = "tester2@example.com"
    # Act
    r = client.post("/activities/NonExistent/signup", params={"email": email})
    # Assert
    assert r.status_code == 404
    assert r.json().get("detail") == "Activity not found"


def test_signup_already_signed_up_returns_400(client):
    # Arrange
    email = "michael@mergington.edu"
    # Act
    r = client.post("/activities/Chess%20Club/signup", params={"email": email})
    # Assert
    assert r.status_code == 400
    assert r.json().get("detail") == "Student is already signed up for this activity"


def test_signup_without_email_returns_422(client):
    # Arrange / Act
    r = client.post("/activities/Chess%20Club/signup")
    # Assert
    assert r.status_code == 422
