import unittest
from jotto import utils

class UtilsTestCase(unittest.TestCase):
    def test_matching_letter_count(self):
        self.assertEqual(utils.matching_letter_count('house', 'haunt'), 2)

    def test_zero_letters_match(self):
        self.assertEqual(utils.matching_letter_count('house', 'strip'), 0)

    def test_word_length_exception_for_short_words(self):
        self.assertRaises(utils.WordLengthException, utils.matching_letter_count, 'house', 'huh')

    def test_word_length_exception_for_long_words(self):
        self.assertRaises(utils.WordLengthException, utils.matching_letter_count, 'house', 'building')


