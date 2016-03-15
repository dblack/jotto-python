import unittest
from jotto.jotto import Game
from jotto.utils import *

class JottoTestCase(unittest.TestCase):
	def setUp(self):
		self.game = Game()

	def test_matching_letter_count(self):
		"""How many matches are there between words?"""

		self.assertEqual(matching_letter_count('house', 'haunt'), 2)

	def test_zero_letters_match(self):
		"""No letters match positionally"""

		self.assertEqual(matching_letter_count('house', 'strip'), 0)

	def test_word_length_exception_for_short_words(self):
		"""Raise exception if word too short"""

		self.assertRaises(WordLengthException, matching_letter_count, 'house', 'huh')

	def test_word_length_exception_for_long_words(self):
		"""Raise exception if word too long"""

		self.assertRaises(WordLengthException, matching_letter_count, 'house', 'building')

	def test_dictionary_words_are_all_five_letters(self):
		dict = self.game.computer.dictionary.words
		over_five = [word for word in dict if len(word.strip()) > 5]
		self.assertEqual(len(over_five), 0)

	def test_winnow_dictionary(self):
		self.game.computer.dictionary.words = ['haunt', 'sense', 'strip', 'every']
		self.game.computer.winnow_dictionary('house', 2)
		self.assertEqual(['haunt', 'sense'], self.game.computer.dictionary.words)