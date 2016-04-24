import utils

class Scorer():
    def score_word(self, guess, index):
        my_word = utils.load_dictionary()[index]
        return utils.correct_letter_count(my_word, guess)
