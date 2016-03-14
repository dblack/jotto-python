import random

class WordLengthException(Exception):
	def __init__(self):
		Exception.__init__(self, "Jotto words have to have exactly five letters")

class Game():
	def load_dictionary(self, filename="fives"):
		self.dictionary = [w.strip() for w in open(filename).readlines()]
		self.players_dictionary = self.dictionary[:]

	def choose_my_word(self):
		self.my_word = random.choice(self.dictionary)

	def matching_letter_count(self, word1, word2):
		if len(word1) != 5 or len(word2) != 5:
			raise WordLengthException()

		return len([n for n in range(0,5) if word1[n] == word2[n]])

	def winnow_dictionary(self, word, count):
		self.dictionary = [w for w in self.dictionary if self.matching_letter_count(word, w) == count]

	def get_guess_from_player(self):
		self.player_guess = input("Your guess: ")

	def guess_players_word(self):
		self.choose_my_word()
		count = int(input(self.my_word + " Count: "))
		self.winnow_dictionary(self.my_word, count)
		return count

	def play(self):
		self.load_dictionary()
		while count != 5:
			count = self.guess_players_word()
		print("I win")
