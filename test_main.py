from fastapi.testclient import TestClient
from main import app  # Adjust the import according to your project structure

client = TestClient(app)

def test_predict_humor():
    response = client.post(
        "/predict/",
        json={"text": "Is this question humorous?"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "question": "Is this question humorous?",
        "prediction": "humorous"  # or "not humorous", depending on your model's prediction
    }

def test_predict_humor_validation_error():
    response = client.post("/predict/", json={})
    assert response.status_code == 422


def test_predict_humor_with_empty_string():
    response = client.post("/predict/", json={"text": ""})
    # Depending on how your model handles empty strings, adjust the expected response accordingly
    assert response.status_code == 200
    assert response.json()["prediction"] in ["humorous", "not humorous"]

def test_predict_humor_with_long_string():
    long_text = "Is this question humorous? " * 100  # A long string to test handling of long inputs
    response = client.post("/predict/", json={"text": long_text})
    assert response.status_code == 200
    assert response.json()["prediction"] in ["humorous", "not humorous"]


def test_predict_humor_with_special_characters():
    response = client.post("/predict/", json={"text": "### ??? !!! ***"})
    assert response.status_code == 200
    assert response.json()["prediction"] in ["humorous", "not humorous"]


def test_predict_humor_with_non_english_text():
    response = client.post("/predict/", json={"text": "これは面白い質問ですか？"})  # "Is this a funny question?" in Japanese
    assert response.status_code == 200
    assert response.json()["prediction"] in ["humorous", "not humorous"]

def test_predict_humor_incorrect_field_name():
    response = client.post("/predict/", json={"question": "Is this humorous?"})
    assert response.status_code == 422  # Expecting a validation error due to incorrect field name

def test_predict_humor_no_data():
    response = client.post("/predict/", data={})
    assert response.status_code == 422  # Expecting a validation error due to missing "text" field
