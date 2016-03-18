import utils, dictionary

class Player(object):
    pass

class Human(Player):
    def valid_guess(self):
        return len(self.current_guess) == 5 and self.current_guess in(dictionary.Dictionary.reference_list)

    def guess_computers_word(self):
        self.current_guess = raw_input("Your guess: ")
        while not self.valid_guess():
            print "Five-letter words from the dictionary only"
            self.current_guess = raw_input("Your guess: ")

class Computer(Player, dictionary.DictionaryOwner):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.guessed_humans_word = False
        self.secret_word = self.choose_a_word()

    def choose_a_word(self):
        return self.dictionary.random_word()

    def report_hits(self, guess):
        print utils.matching_letter_count(guess, self.secret_word)

    def guess_humans_word(self):
        guess = self.choose_a_word()
        count = int(raw_input(guess + ": "))

        self.dictionary.winnow(guess, count)
        self.guessed_humans_word = count == 5