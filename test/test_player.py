import unittest
import sys
from StringIO import StringIO
from jotto import player
from contextlib import contextmanager

class HumanTestCase(unittest.TestCase):
    def setUp(self):
        self.human = player.Human()

    def test_guess_to_short_a_word(self):
        self.guess_a_word("tiny")

    def test_guess_too_long_a_word(self):
        self.guess_a_word("lengthy")

    def test_guess_a_nonexistent_word(self):
        self.guess_a_word("blaha")

    def guess_a_word(self, word):
        with self.switch_io(word + "\nright") as output_stream:
            self.human.guess_computers_word()
 
        self.assertEqual(output_stream.read(), "Your guess: Five-letter words from the dictionary only\nYour guess: ")
        self.assertEqual(self.human.current_guess, "right")

    @contextmanager
    def switch_io(self, input_string):
        sys.stdin = StringIO(input_string)
        output_stream = StringIO()
        sys.stdout = output_stream

        yield output_stream

        output_stream.seek(0)
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
