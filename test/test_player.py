import unittest
import sys
import __builtin__
from mock import patch
from StringIO import StringIO
from jotto import player

class HumanTestCase(unittest.TestCase):
    def setUp(self):
        self.human = player.Human()

    def test_guess_unacceptable_words(self):
        for word in ('tiny', 'lengthy', 'blaha'):
            with patch('__builtin__.raw_input', side_effect=(word, 'right')):
                self.guess_a_word()

    def guess_a_word(self):
        with patch('sys.stdout', new=StringIO()) as temp_out:
            self.human.guess_computers_word()

        self.assertEqual(self.human.current_guess, "right")
        self.assertEqual(temp_out.getvalue(), "Five-letter words from the dictionary only\n")