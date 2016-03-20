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
            for guess, count in self.filters:
                if utils.matching_letter_count(word, guess) is not count:
                    return False
            return True

        with open(self.filename) as fh:
            for word in fh:
                word = word.strip()
                if include_word(word):
                    yield(word)

    def random_word(self):
        offset = random.choice(range(0, len(self)) )
        for index, word in enumerate(self):
            if index == offset:
                return word

    def winnow(self, guess, count):
        if count > 0:
            self.filters.append((guess, count))

class DictionaryOwner(object):
    def __init__(self):
        self.dictionary = Dictionary()