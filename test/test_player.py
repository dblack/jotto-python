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