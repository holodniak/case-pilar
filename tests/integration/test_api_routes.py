import pytest
from fastapi.testclient import TestClient
from app import app

@pytest.fixture
def client():
    return TestClient(app)

class TestVowelCountEndpoint:
    def test_count_vowels_success(self, client):
        response = client.post(
            "/api/v1/vowel_count",
            json={"words": ["desenvolvimento", "tecnologia", "inovacao"]}
        )
        assert response.status_code == 200
        assert response.json() == {
            "desenvolvimento": 6,
            "tecnologia": 5,
            "inovacao": 5
        }
    
    def test_count_vowels_invalid_json(self, client):
        response = client.post(
            "/api/v1/vowel_count",
            content="invalid json",
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 422
    
class TestSortEndpoint:
    def test_sort_words_success_asc(self, client):
        response = client.post(
            "/api/v1/sort",
            json={
                "words": ["python", "java", "rust"],
                "order": "asc"
            }
        )
        assert response.status_code == 200
        assert response.json() == ["java", "python", "rust"]
    
    def test_sort_words_success_desc(self, client):
        response = client.post(
            "/api/v1/sort",
            json={
                "words": ["python", "java", "rust"],
                "order": "desc"
            }
        )
        assert response.status_code == 200
        assert response.json() == ["rust", "python", "java"]
    
    def test_sort_words_invalid_order(self, client):
        response = client.post(
            "/api/v1/sort",
            json={
                "words": ["python", "java", "rust"],
                "order": "invalid"
            }
        )
        assert response.status_code == 422
        error_detail = response.json()["detail"]
        assert error_detail["field"] == "order"
        assert "asc" in error_detail["message"] and "desc" in error_detail["message"]

class TestErrorHandling:
    def test_route_not_found(self, client):
        response = client.get("/api/v1/invalid")
        assert response.status_code == 404
        assert "Not Found" in response.json()["detail"]
    
    def test_method_not_allowed(self, client):
        response = client.get("/api/v1/vowel_count")
        assert response.status_code == 405
        assert "Method Not Allowed" in response.json()["detail"]
        assert "POST" in response.headers["allow"]