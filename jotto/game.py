import player

class Game():
    def __init__(self):
        self.computer = player.Computer()
        self.human = player.Human()
        self.humans_current_guess = ""

    def computer_wins(self):
        return self.computer.guessed_players_word

    def human_wins(self):
        return self.humans_current_guess == self.computer.secret_word

    def game_in_progress(self):
        return not self.computer_wins() and not self.human_wins()

    def tie(self):
        return self.human_wins() and self.computer_wins()

    def play(self):
        while self.game_in_progress():
            self.human.guess_computers_word()
            self.computer.report_hits(self.human.current_guess)
            self.computer.guess_players_word()

        if self.tie():
            print "Tie!"
        elif self.human_wins():
            print "You win!"
        else:
            print "I win! My word was " + self.computer.secret_word
