from random import randint

class SecretWord():
    def __init__(self, event):
        self.event = event

    def get(self):
        words = self.load_dictionary()
        return words[int(self.event.get('pathIndex', randint(0, len(words) - 1)))]

    def load_dictionary(self, filename = 'fives.shuffled'):
        with open(filename) as fh:
            words = [word.rstrip() for word in fh.readlines()]
        return words    
