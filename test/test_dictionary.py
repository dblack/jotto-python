import unittest
from jotto import game
from jotto import dictionary

class DictionaryTestCase(unittest.TestCase):
    def setUp(self):
        self.dictionary = dictionary.Dictionary()

    def test_dictionary_words_are_all_five_letters(self):
        dict = self.dictionary.words
        over_five = [word for word in dict if len(word.strip()) > 5]
        self.assertEqual(len(over_five), 0)

    def test_winnow_dictionary(self):
        self.dictionary.words = ['haunt', 'sense', 'strip', 'every']
        self.dictionary.winnow('house', 2)
        self.assertEqual(['haunt', 'sense'], self.dictionary.words)