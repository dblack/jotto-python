import utils, dictionary

class Player(dictionary.DictionaryOwner):
	pass

class Computer(Player):
	def choose_a_word(self):
		return self.dictionary.random_word()

	def winnow_dictionary(self, word, count):
		self.dictionary.words = [w for w in self.dictionary.words if utils.matching_letter_count(word, w) == count]

	def get_guess_from_player(self):
		self.player_guess = input("Your guess: ")

	def guess_players_word(self):
		guess = self.choose_a_word()
		count = int(input(guess + ": "))
		self.winnow_dictionary(guess, count)
		return count

class Human(Player):
	pass
