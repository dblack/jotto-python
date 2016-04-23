from random import randint

class SecretWord():
    def __init__(self, data):
        self.data = data
        self.words = self.load_dictionary()

    def index(self):
        return int(self.data.get('pathIndex', randint(0, len(self.words) - 1)))

    def word(self):
        return self.words[self.index()]

    def load_dictionary(self, filename = 'fives.shuffled'):
        with open(filename) as fh:
            words = [word.rstrip() for word in fh.readlines()]
        return words    
