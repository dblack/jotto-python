import random
import utils

class Dictionary():
	def __init__(self, filename="jotto/fives"):
		with open(filename) as fh:
			self.words = [w.strip() for w in fh]

	def random_word(self):
		return random.choice(self.words)

	def winnow(self, word, count):
		self.words = [w for w in self.words if utils.matching_letter_count(word, w) == count]


class DictionaryOwner():
	def __init__(self):
		self.dictionary = Dictionary()