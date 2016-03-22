import unittest
import sys
from __builtin__ import raw_input
from mock import patch
from StringIO import StringIO
from jotto import player
from jotto.keyboard_io import KeyboardIO

class HumanTestCase(unittest.TestCase):
    def setUp(self):
        self.human = player.Human()

    def test_guess_unacceptable_words(self):
        good_word = 'right'
        for bad_word in ('tiny', 'lengthy', 'blaha'):
            with patch('jotto.keyboard_io.KeyboardIO.get_input', side_effect=(bad_word, good_word)):
                self.guess_a_word()

    def guess_a_word(self):
        with patch('sys.stdout', new=StringIO()) as temp_out:
            self.human.guess_computers_word()

        self.assertEqual(self.human.current_guess, "right")
        self.assertEqual(temp_out.getvalue(), "Five-letter words from the dictionary only\n")

    def test_short_word_is_invalid(self):
        self.human.dictionary = ['tiny', 'house', 'mouse', 'inset', 'bring']
        self.human.guess_a_word('tiny')
        self.assertFalse(self.human.valid_guess())

    def test_long_word_is_invalid(self):
        self.human.dictionary = ['lengthy', 'house', 'mouse', 'inset', 'bring']
        self.human.guess_a_word('lengthy')
        self.assertFalse(self.human.valid_guess())

    def test_non_dictionary_word_is_invalid(self):
        self.human.dictionary = ['house', 'mouse', 'inset', 'bring']
        self.human.guess_a_word('touse')
        self.assertFalse(self.human.valid_guess())

    def test_five_letter_word_in_dictionary_is_valid(self):
        self.human.dictionary = ['house', 'mouse', 'inset', 'bring']
        self.human.guess_a_word('house')
        self.assertTrue(self.human.valid_guess())

