import unittest
import sys
from __builtin__ import raw_input
from mock import patch
from StringIO import StringIO
import player
import keyboard_io

class HumanTestCase(unittest.TestCase):
    def setUp(self):
        self.human = player.Human()

    def test_guess_unacceptable_words(self):
        good_word = 'right'
        for bad_word in ('tiny', 'lengthy', 'blaha'):
            with patch('keyboard_io.KeyboardIO.get_input', side_effect=(bad_word, good_word)):
                self.guess_a_word()

    def guess_a_word(self):
        with patch('sys.stdout', new=StringIO()) as temp_out:
            self.human.guess_computers_word()

        self.assertEqual(self.human.current_guess, "right")
        self.assertEqual(temp_out.getvalue(), "Five-letter words from the dictionary only\n")

