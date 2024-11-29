from anagram import AnagramFinder

if __name__ == "__main__":
    text = input("Введите текст: ")
    finder = AnagramFinder(text)
    results = finder.find_anagrams()
    print(finder.display_results(results))