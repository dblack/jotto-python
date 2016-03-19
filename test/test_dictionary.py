import unittest
from jotto import game, dictionary

class DictionaryTestCase(unittest.TestCase):
    def setUp(self):
        self.dictionary = dictionary.Dictionary()

    def test_dictionary_words_are_all_five_letters(self):
        not_five_letter_words = [word for word in self.dictionary.words if len(word.strip()) is not 5]
        self.assertFalse(not_five_letter_words)

    def test_winnow_dictionary(self):
        self.dictionary.words = ['haunt', 'sense', 'strip', 'every']
        self.dictionary.winnow('house', 2)
        self.assertEqual(['haunt', 'sense'], self.dictionary.words)