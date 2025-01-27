class TextService:
    @staticmethod
    def count_vowels(words: list[str]) -> dict:
        vowels = set("aeiouAEIOU")
        result = {}

        for word in words:
            count = sum(1 for char in word if char in vowels)
            result[word] = count

        return result

    @staticmethod
    def sort_words(words: list[str], order: str) -> list[str]:
        reverse = order == "desc"
        return sorted(words, reverse=reverse)
