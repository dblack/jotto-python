class Dictionary():
	def __init__(self, filename="jotto/fives"):
		with open(filename) as fh:
			self.words = [w.strip() for w in fh]

	def random_word(self):
		return random.choice(self.words)

class DictionaryOwner():
	def __init__(self):
		self.dictionary = Dictionary()