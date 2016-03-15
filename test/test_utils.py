import unittest
import jotto
from jotto import utils

class UtilsTestCase(unittest.TestCase):
	def test_matching_letter_count(self):
		"""How many matches are there between words?"""

		self.assertEqual(utils.matching_letter_count('house', 'haunt'), 2)

	def test_zero_letters_match(self):
		"""No letters match positionally"""

		self.assertEqual(utils.matching_letter_count('house', 'strip'), 0)

	def test_word_length_exception_for_short_words(self):
		"""Raise exception if word too short"""

		self.assertRaises(utils.WordLengthException, jotto.utils.matching_letter_count, 'house', 'huh')

