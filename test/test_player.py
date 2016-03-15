import unittest
import player

class ComputerTestCase(unittest.TestCase):
    def setUp(self):
        self.computer = player.Computer()

    def test_valid_player_guess(self):
        self.computer.player_guess = "tiny"
        self.assertEqual(self.computer.valid_player_guess(), False)

        self.computer.player_guess = "lengthy"
        self.assertEqual(self.computer.valid_player_guess(), False)

        self.computer.player_guess = "right"
        self.assertEqual(self.computer.valid_player_guess(), True)       