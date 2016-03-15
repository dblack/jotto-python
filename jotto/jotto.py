import random
from utils import *

class Dictionary():
	def __init__(self, filename="jotto/fives"):
		self.words = [w.strip() for w in open(filename).readlines()]

	def random_word(self):
		return random.choice(self.words)

class DictionaryOwner():
	def __init__(self):
		self.dictionary = Dictionary()

class Player():
	pass

class Computer(DictionaryOwner, Player):
	def choose_my_word(self):
		self.my_word = self.dictionary.random_word()

	def winnow_dictionary(self, word, count):
		self.dictionary.words = [w for w in self.dictionary.words if matching_letter_count(word, w) == count]

	def guess_players_word(self):
		self.choose_my_word()
		count = int(input(self.my_word + " Count: "))
		self.winnow_dictionary(self.my_word, count)
		return count

class Human(DictionaryOwner, Player):
	pass

class Game():
	def __init__(self):
		self.computer = Computer()
		self.human = Human()

	def get_guess_from_player(self):
		self.player_guess = input("Your guess: ")

	def play(self):
		count = 0
		while count != 5:
			count = self.computer.guess_players_word()
		print("I win")
