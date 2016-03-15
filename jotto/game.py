import player, utils

class Game():
	def __init__(self):
		self.computer = player.Computer()
		self.human = player.Human()

	def play(self):
		self.computer.word = self.computer.choose_a_word()
		count = 0
		self.player_guess = ""
		player_wins = False

		while (count != 5) and (player_wins == False):
			self.computer.get_guess_from_player()
			print(utils.matching_letter_count(self.computer.player_guess, self.computer.word))
			player_wins = self.computer.player_guess == self.computer.word
			count = self.computer.guess_players_word()

		if player_wins:
			print("You win!")
		else:
			print("I win! My word was " + self.computer.word)
