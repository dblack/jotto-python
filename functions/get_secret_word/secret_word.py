from random import randint

class SecretWord():
    def __init__(self, event):
        self.event = event

    def get(self):
        words = self.load_dictionary()
        if 'pathIndex' in self.event:
            index = int(self.event['pathIndex'])
        else:
            index = randint(0, len(words) - 1)
        return words[index]

    def load_dictionary(self):
        with open('fives.shuffled') as fh:
            words = [word.rstrip() for word in fh.readlines()]
        return words    
