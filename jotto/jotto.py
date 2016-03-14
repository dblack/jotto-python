class WordLengthException(Exception):
	def __init__(self):
		Exception.__init__(self, "Jotto words have to have exactly five letters")

class Game():
	def load_dictionary(self, filename="fives"):
		self.dictionary = [w.strip() for w in open(filename).readlines()]

	def matching_letter_count(self, word1, word2):
		if len(word1) != 5 or len(word2) != 5:
			raise WordLengthException()

		return len([n for n in range(0,5) if word1[n] == word2[n]])

	def winnow_dictionary(self, word, count):
		self.dictionary = [w for w in self.dictionary if self.matching_letter_count(word, w) != count ]