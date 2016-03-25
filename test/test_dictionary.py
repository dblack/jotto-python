import unittest
import mock
import guess, game, dictionary

class DictionaryTestCase(unittest.TestCase):
    def setUp(self):
        self.dictionary = dictionary.Dictionary()

    def test_dictionary_words_are_all_five_letters(self):
        not_five_letter_words = (word for word in self.dictionary if len(word.strip()) is not 5)
        self.assertFalse(list(not_five_letter_words))

    def test_winnow_dictionary(self):
        self.dictionary.winnow(guess.Guess('house'), 5)
        self.assertEqual(len(self.dictionary), 1)
        self.assertEqual('house', next(self.dictionary.__iter__()))