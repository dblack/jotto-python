import random
import utils

class Dictionary():
    def __init__(self, filename="jotto/fives"):
        self.filename = filename
        self.filters = []

    def __len__(self):
        for index, word in enumerate(self, 1):
            pass
        return index

    def __iter__(self):
        def include_word(word):
            if not self.filters:
                return True
            for guess, count in self.filters:
                if utils.matching_letter_count(word, guess) is count:
                    return True
            return False

        with open(self.filename) as fh:
            for word in fh:
                word = word.rstrip()
                if include_word(word):
                    yield(word)

    def random_word(self):
        offset = random.choice(range(0, len(self)) )
        for index, word in enumerate(self):
            if index == offset:
                return word

    def winnow(self, guess, count):
        self.filters.append((guess, count))

class DictionaryOwner(object):
    def __init__(self):
        self.dictionary = Dictionary()