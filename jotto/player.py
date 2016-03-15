import utils, dictionary

class Player(dictionary.DictionaryOwner):
    pass

class Computer(Player):
    def choose_a_word(self):
        return self.dictionary.random_word()

    def valid_player_guess(self):
        return len(self.player_guess) == 5

    def get_guess_from_player(self):
        self.player_guess = input("Your guess: ")
        while not self.valid_player_guess():
            print("Five-letter words only")
            self.player_guess = input("Your guess: ")

    def guess_players_word(self):
        guess = self.choose_a_word()
        count = int(input(guess + ": "))
        self.dictionary.winnow(guess, count)
        return count

class Human(Player):
    pass
