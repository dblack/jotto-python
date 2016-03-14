import unittest
import jotto
from jotto.jotto import matching_letter_count

class JottoTestCase(unittest.TestCase):
	def test_matching_letter_count(self):
		"""How many matches are there between words?"""
		word1 = 'house'
		word2 = 'haunt'

		self.assertEqual(matching_letter_count(word1, word2), 2)

	def test_zero_letters_match(self):
		"""No letters match positionally"""
		word1 = 'house'
		word2 = 'strip'

		self.assertEqual(matching_letter_count(word1, word2), 0)

	def test_word_length_exception_for_short_words(self):
		"""Raise exception if word too short"""

		self.assertRaises(jotto.jotto.WordLengthException, jotto.jotto.matching_letter_count, 'house', 'huh')

	def test_word_length_exception_for_long_words(self):
		"""Raise exception if word too long"""

		self.assertRaises(jotto.jotto.WordLengthException, jotto.jotto.matching_letter_count, 'house', 'building')
