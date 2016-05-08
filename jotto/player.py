import requests
import re
import sys, os
import json

sys.path.insert(0, '../functions')
import utils
from keyboard_io import KeyboardIO

base_url = 'https://b578bine84.execute-api.us-east-1.amazonaws.com/dev'
secret_word_url = base_url + '/get_secret_word'
score_guess_url = base_url + '/score_humans_guess'
guess_word_url = base_url + '/guess_humans_word'


class Human():
    def __init__(self):
        self.current_guess = ""

    def guess_computers_word(self):
        self.current_guess = KeyboardIO.get_input("Your guess: ")

class Computer():
    def __init__(self):
        self.guessed_humans_word = False
        self.guess_history = ""
        self.choose_a_word()

    def choose_a_word(self):
        data = utils.response_object(secret_word_url)
        self.secret_word = data["word"]
        print self.secret_word
        self.word_index = int(data["index"])

    def report_hits(self, guess):
        url = "{}/{}/{}".format(score_guess_url, guess, self.word_index)
        response = requests.get(url)
        return int(response.json()['score'])

    def get_count_from_human(self, guess):
        return int(KeyboardIO.get_input(guess + ": "))

    def guess_humans_word(self):
        data = utils.response_object("{}/{}".format(guess_word_url, self.guess_history))
        guess = data["guess"]
        match_count = self.get_count_from_human(guess)
        self.guess_history = self.guess_history + guess + str(match_count)
        self.guessed_humans_word = match_count is 5
