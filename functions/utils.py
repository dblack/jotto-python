import requests
import json

def load_dictionary(filename = 'lib/fives.shuffled'):
    with open(filename) as fh:
        return [word.rstrip() for word in fh.readlines()]

def correct_letter_count(word, guess):
    return len([True for char1, char2 in zip(word, guess) if char1 == char2])

def response_object(url):
    response = requests.get(url)
    response.encoding = 'ISO-8859-1'
    return json.loads(response.text)
