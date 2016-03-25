import unittest
import guess

class GuessTestCase(unittest.TestCase):
    def setUp(self):
        self.guess = guess.Guess('house')

    def test_matching_letter_count(self):
        self.assertEqual(self.guess.correct_letter_count('haunt'), 2)

    def test_zero_letters_match(self):
        self.assertEqual(self.guess.correct_letter_count('strip'), 0)

    def test_short_word_is_invalid(self):
        a_guess = guess.Guess('tiny')
        a_guess.dictionary = ['tiny', 'house', 'mouse', 'inset', 'bring']
        self.assertFalse(a_guess.valid())

    def test_long_word_is_invalid(self):
        a_guess = guess.Guess('lengthy')
        a_guess.dictionary = ['lengthy', 'house', 'mouse', 'inset', 'bring']        
        self.assertFalse(a_guess.valid())

    def test_non_dictionary_word_is_invalid(self):
        a_guess = guess.Guess('blaha')
        a_guess.dictionary = ['house', 'mouse', 'inset', 'bring']        
        self.assertFalse(a_guess.valid())

    def test_five_letter_dictionary_word_is_valid(self):
        a_guess = guess.Guess('house')
        a_guess.dictionary = ['house', 'mouse', 'inset', 'bring']        
        self.assertTrue(a_guess.valid())
