import random
import utils

class Dictionary():
    with open("jotto/fives") as fh:
        reference_list = [w.strip() for w in fh]

    def __init__(self, filename="jotto/fives"):
        self.words = Dictionary.reference_list[:]

    def random_word(self):
        return random.choice(self.words)

    def winnow(self, word, count):
        self.words = [w for w in self.words if utils.matching_letter_count(word, w) == count]

class DictionaryOwner(object):
    def __init__(self):
        self.dictionary = Dictionary()