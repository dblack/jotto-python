
import dictionary, guess
import requests
import re

from keyboard_io import KeyboardIO

regex = '\w{5}'
url = 'https://b578bine84.execute-api.us-east-1.amazonaws.com/dev/get_secret_word/'

class Human():
    def __init__(self):
        self.guess_a_word("")

    def guess_computers_word(self):
        while True:
            self.see_prompt_and_enter_guess()

            if self.current_guess.valid():
                break
            else:
                print "Five-letter words from the dictionary only"

    def guess_a_word(self, word):
        self.current_guess = guess.Guess(word)

    def see_prompt_and_enter_guess(self):
        self.guess_a_word(KeyboardIO.get_input("Your guess: "))

class Computer(dictionary.DictionaryOwner):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.guessed_humans_word = False
        self.secret_word = self.choose_a_word()

    def choose_a_word(self):
        raw_word = str(requests.get(url).text)
        return re.search(regex, raw_word).group()

    def report_hits(self, guess):
        return guess.correct_letter_count(self.secret_word)

    def get_count_from_human(self, guess):
        return int(KeyboardIO.get_input(guess + ": "))

    def guess_humans_word(self):
        a_guess = self.choose_a_word()
        match_count = self.get_count_from_human(a_guess)

        self.dictionary.winnow(guess.Guess(a_guess), match_count)
        self.guessed_humans_word = match_count is 5