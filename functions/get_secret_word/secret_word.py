from random import randint

class SecretWord():
    def __init__(self, data):
        self.data = data
        self.words = self.load_dictionary()
        self.index = self.get_index()
        self.word = self.get_word()

    def get_index(self):
        return int(self.data.get('pathIndex', randint(0, len(self.words) - 1)))

    def get_word(self):
        return self.words[self.index]

    def load_dictionary(self, filename = 'lib/fives.shuffled'):
        with open(filename) as fh:
            return [word.rstrip() for word in fh.readlines()]
