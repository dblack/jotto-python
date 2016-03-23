import dictionary

class Guess(dictionary.DictionaryOwner):
    def __init__(self, string):
        self.dictionary = dictionary.Dictionary()
        self.string = string

    def __len__(self):
        return len(self.string)

    def __iter__(self):
        for char in self.string:
            yield(char)

    def __eq__(self, word):
        return self.string is word

    def in_dictionary(self):
        return self.string in self.dictionary

    def five_letters_long(self):
        return len(self) is 5

    def valid(self):
        return self.five_letters_long() and self.in_dictionary()

    def correct_letter_count(self, word):
        return len([True for char1, char2 in zip(self, word) if char1 == char2])
