import unittest
import jotto
from jotto.jotto import matching_letter_count

class JottoTestCase(unittest.TestCase):
	def test_matching_letter_count(self):
		"""How many matches are there between words?"""
		word1 = 'house'
		word2 = 'haunt'

		self.assertEqual(jotto.jotto.matching_letter_count(word1, word2), 2)
