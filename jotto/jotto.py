import random
import jotto.player

class Game():
	def __init__(self):
		self.computer = jotto.player.Computer()
		self.human = jotto.player.Human()

	def get_guess_from_player(self):
		self.player_guess = input("Your guess: ")

	def play(self):
		count = 0
		while count != 5:
			count = self.computer.guess_players_word()
		print("I win")
