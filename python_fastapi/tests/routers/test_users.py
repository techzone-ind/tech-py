from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_post_user():
    payload = {
        "username": "Tester1",
        "email": "test@t1.com",
        "sport": "Cricket",
        "password": "12345"
    }
    #headers = {"X-Process-Token": "test"}
    response = client.post("/users/", json=payload)
    assert response.status_code == 200
    res = response.json()
    assert res['username'] == "Tester1"
    assert res['email'] == "test@t1.com"

def test_get_user():
    response = client.get("/users/")
    assert response.status_code == 200
    res = response.json()   
    assert len(res) == 3
    assert res[0]['username'] == "Ram"