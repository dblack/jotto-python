import player

class Game():
    def __init__(self):
        self.computer = player.Computer()
        self.computer.choose_secret_word()

    def computer_wins(self):
        return self.computer.guessed_players_word

    def human_wins(self):
        return self.computer.human_guess == self.computer.word

    def no_winner(self):
        return not self.computer_wins() and not self.human_wins()

    def play(self):
        while self.no_winner():
            self.computer.get_guess_from_player()
            self.computer.report_hits()
            self.computer.guess_players_word()

        if self.human_wins():
            print("You win!")
        else:
            print("I win! My word was " + self.computer.word)
