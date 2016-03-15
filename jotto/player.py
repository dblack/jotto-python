import utils, dictionary

class Player():
	pass

class Computer(dictionary.DictionaryOwner, Player):
	def choose_my_word(self):
		self.my_word = self.dictionary.random_word()

	def winnow_dictionary(self, word, count):
		self.dictionary.words = [w for w in self.dictionary.words if utils.matching_letter_count(word, w) == count]

	def guess_players_word(self):
		self.choose_my_word()
		count = int(input(self.my_word + " Count: "))
		self.winnow_dictionary(self.my_word, count)
		return count

class Human(dictionary.DictionaryOwner, Player):
	pass
