import sys, os
sys.path.append(sys.path.insert(0, os.path.dirname(__file__)))
print(sys.path)
import pytest
import requests
from .. import secret_word

url = 'https://b578bine84.execute-api.us-east-1.amazonaws.com/dev/get_secret_word/'

def test_getting_specific_word():
    index = 100
    with open('functions/get_secret_word/fives.shuffled') as fh:
        words = [word.rstrip() for word in fh]
    word = words[index]

    response = requests.get(url + str(index))
    assert response.text == '"{}"'.format(word)
