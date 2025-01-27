import pytest
from app.services.text_service import TextService

@pytest.fixture
def service():
    return TextService()

class TestTextService:
    def test_count_vowels_with_valid_words(self, service):
        words = ["desenvolvimento", "tecnologia", "inovacao"]
        result = service.count_vowels(words)
        
        assert result == {
            "desenvolvimento": 6,
            "tecnologia": 5,
            "inovacao": 5
        }
    
    def test_count_vowels_with_empty_word(self, service):
        words = [""]
        result = service.count_vowels(words)
        assert result == {"": 0}
    
    def test_count_vowels_with_no_vowels(self, service):
        words = ["txt", "php", "css"]
        result = service.count_vowels(words)
        assert result == {"txt": 0, "php": 0, "css": 0}
        
    def test_sort_words_ascending(self, service):
        words = ["python", "java", "rust"]
        result = service.sort_words(words, "asc")
        assert result == ["java", "python", "rust"]
    
    def test_sort_words_descending(self, service):
        words = ["python", "java", "rust"]
        result = service.sort_words(words, "desc")
        assert result == ["rust", "python", "java"]
        
    def test_sort_words_with_empty_list(self, service):
        words = []
        result = service.sort_words(words, "asc")
        assert result == [] 