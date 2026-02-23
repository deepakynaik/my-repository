def test_root_redirects_to_static_index(client):
    # Arrange
    # Act (do not follow redirects)
    r = client.get("/", follow_redirects=False)
    # Assert
    assert r.status_code in (307, 302)
    assert "/static/index.html" in r.headers.get("location", "")


def test_get_activities_returns_dict(client):
    # Arrange
    # Act
    r = client.get("/activities")
    # Assert
    assert r.status_code == 200
    data = r.json()
    assert "Chess Club" in data
