import re
import random

import utils

HISTORY_RE = re.compile(r'(\w{5})(\d+)')

class Guess():

    def __init__(self, history_string):
        self.history_string = history_string
        self.history = self.parse_history_string()

    def parse_history_string(self):
        elements = [x for x in HISTORY_RE.split(self.history_string) if x]
        return dict(zip(elements[::2], elements[1::2]))

    def make_guess(self):
        return random.choice(self.load_filtered_dictionary())

    def include_word(self, word):
        for guess, count in self.history.items():
            if (utils.correct_letter_count(word, guess)) is not int(count):
                return False
        return True

    def load_filtered_dictionary(self, filename = 'lib/fives.shuffled'):
        with open(filename) as fh:
            return [word.rstrip() for word in fh.readlines() if self.include_word(word)]

