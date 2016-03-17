import utils, dictionary

class Computer(dictionary.DictionaryOwner):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.guessed_players_word = False
        self.human_guess = ""

    def choose_a_word(self):
        return self.dictionary.random_word()

    def choose_secret_word(self):
        self.word = self.choose_a_word()

    def valid_player_guess(self):
        return len(self.player_guess) == 5 and self.player_guess in(dictionary.Dictionary.reference_list)

    def get_guess_from_player(self):
        self.player_guess = raw_input("Your guess: ")
        while not self.valid_player_guess():
            print("Five-letter words from the dictionary only")
            self.player_guess = raw_input("Your guess: ")

    def report_hits(self):
        print(utils.matching_letter_count(self.player_guess, self.word))

    def guess_players_word(self):
        guess = self.choose_a_word()
        count = int(raw_input(guess + ": "))

        self.dictionary.winnow(guess, count)
        self.guessed_players_word = count == 5