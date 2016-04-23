import sys, os
import pytest
import requests

from .. import secret_word

filedir = os.path.dirname(__file__)
parentdir = os.path.dirname(filedir)

sys.path.append(sys.path.insert(0, filedir))

url = 'https://b578bine84.execute-api.us-east-1.amazonaws.com/dev/get_secret_word/'

def test_getting_specific_word():
    index = 100
    with open(parentdir + '/fives.shuffled') as fh:
        words = [word.rstrip() for word in fh]
    word = words[index]

    response = requests.get(url + str(index))
    assert response.text == '{"index": 100, "word": "unsay"}'
