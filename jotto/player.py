import utils, dictionary

class Player():
    pass

class Human(Player):
    def valid_guess(self, guess):
        return len(guess) == 5 and guess in(dictionary.Dictionary.reference_list)

    def guess_computers_word(self):
        guess = raw_input("Your guess: ")
        while not self.valid_guess(guess):
            print("Five-letter words from the dictionary only")
            guess = raw_input("Your guess: ")
        return guess

class Computer(Player, dictionary.DictionaryOwner):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.guessed_players_word = False
        self.secret_word = self.choose_a_word()
 
    def choose_a_word(self):
        return self.dictionary.random_word()

    def valid_player_guess(self):
        return len(self.player_guess) == 5 and self.player_guess in(dictionary.Dictionary.reference_list)

    def report_hits(self, guess):
        print(utils.matching_letter_count(guess, self.secret_word))

    def guess_players_word(self):
        guess = self.choose_a_word()
        count = int(raw_input(guess + ": "))

        self.dictionary.winnow(guess, count)
        self.guessed_players_word = count == 5