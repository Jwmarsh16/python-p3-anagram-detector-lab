
class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)

    def match(self, other_word):
        matches = []
        for candidate in other_word:
            if sorted(candidate) == self.sorted_word:
                matches.append(candidate)
        return matches

            


    