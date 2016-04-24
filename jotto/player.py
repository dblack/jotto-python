
import dictionary, guess
import requests
import re
import sys, os
import json

sys.path.insert(0, '../functions')
import utils
from keyboard_io import KeyboardIO

regex = '\w{5}'
secret_word_url = 'https://b578bine84.execute-api.us-east-1.amazonaws.com/dev/get_secret_word'
score_guess_url = 'https://b578bine84.execute-api.us-east-1.amazonaws.com/dev/score_humans_guess'
guess_word_url = 'https://b578bine84.execute-api.us-east-1.amazonaws.com/dev/guess_humans_word'


class Human():
    def __init__(self):
        self.current_guess = ""

    def guess_computers_word(self):
        self.see_prompt_and_enter_guess()

    def see_prompt_and_enter_guess(self):
        self.current_guess = KeyboardIO.get_input("Your guess: ")

class Computer():
    def __init__(self):
        self.guessed_humans_word = False
        self.guess_history = ""
        self.choose_a_word()

    def choose_a_word(self):
        response = requests.get(secret_word_url)
        response.encoding = 'ISO-8859-1'
        data = json.loads(response.text)
        self.secret_word = data["word"]
        self.word_index = int(data["index"])

    def report_hits(self, guess):
        response = requests.get("{}/{}/{}".format(score_guess_url, guess, self.word_index))
        return utils.correct_letter_count(guess, self.secret_word)

    def get_count_from_human(self, guess):
        return int(KeyboardIO.get_input(guess + ": "))

    def guess_humans_word(self):
        response = requests.get("{}/{}".format(guess_word_url, self.guess_history),
            headers = { 'Accept-Charset': 'ISO-8859-1'})
        response.encoding = 'ISO-8859-1'
        guess = json.loads(response.text)["guess"]
        match_count = self.get_count_from_human(guess)
        self.guess_history = self.guess_history + guess + str(match_count)
        self.guessed_humans_word = match_count is 5
