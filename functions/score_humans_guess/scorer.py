class Scorer():
    def score_word(self, guess, index):
        my_word = self.load_dictionary()[index]
        return self.correct_letter_count(my_word, guess)

    def correct_letter_count(self, word, guess):
        return len([True for char1, char2 in zip(word, guess) if char1 == char2])

    def load_dictionary(self, filename = 'fives.shuffled'):
        with open(filename) as fh:
            words = [word.rstrip() for word in fh.readlines()]
        return words    
