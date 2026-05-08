def test_register_user(client):
    response = client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "motdepasse123"
    })
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"
    assert "hashed_password" not in response.json()

def test_login_success(client):
    client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "motdepasse123"
    })
    response = client.post("/auth/login", data={
        "username": "test@example.com",
        "password": "motdepasse123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_wrong_password(client):
    client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "motdepasse123"
    })
    response = client.post("/auth/login", data={
        "username": "test@example.com",
        "password": "mauvaismdp"
    })
    assert response.status_code == 401

def test_get_me_with_token(client):
    client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "motdepasse123"
    })
    login = client.post("/auth/login", data={
        "username": "test@example.com",
        "password": "motdepasse123"
    })
    token = login.json()["access_token"]
    response = client.get("/users/me", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_get_me_without_token(client):
    response = client.get("/users/me")
    assert response.status_code == 401