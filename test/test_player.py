import unittest
import sys
import StringIO
from jotto import player

class HumanTestCase(unittest.TestCase):
    def setUp(self):
        self.human = player.Human()

    def test_valid_guess(self):
        self.human.current_guess = "tiny"
        self.assertEqual(self.human.valid_guess(), False)

        self.human.current_guess = "lengthy"
        self.assertEqual(self.human.valid_guess(), False)

        self.human.current_guess = "right"
        self.assertEqual(self.human.valid_guess(), True)

    def test_guess_computers_word(self):
        input_string = StringIO.StringIO("tiny\nright")
        sys.stdin = input_string
        output_string = StringIO.StringIO()
        sys.stdout = output_string

        self.human.guess_computers_word()

        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        output_string.seek(0)
        self.assertEqual(output_string.readline(), "Your guess: Five-letter words from the dictionary only\n")