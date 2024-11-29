class AnagramFinder:
    def __init__(self, text):
        self.text = text

    def find_anagrams(self):
        words = self.text.split()
        anagrams = {}
        for word in words:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        return {key: value for key, value in anagrams.items() if len(value) > 1}

    def display_results(self, results):
        if results:
            return f"Найденные анаграммы: {results}"
        else:
            return "Анаграммы не найдены."