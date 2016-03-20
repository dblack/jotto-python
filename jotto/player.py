import utils, dictionary

class Player(object):
    pass

class Human(Player, dictionary.DictionaryOwner):
    def guess_has_five_letters(self):
        return len(self.current_guess) is 5

    def guess_is_in_dictionary(self):
        return self.current_guess in(self.dictionary)

    def valid_guess(self):
        return self.guess_has_five_letters() and self.guess_is_in_dictionary()

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
        return utils.matching_letter_count(guess, self.secret_word)

    def guess_humans_word(self):
        guess = self.choose_a_word()
        count = int(raw_input(guess + ": "))

        self.dictionary.winnow(guess, count)
        self.guessed_humans_word = count == 5