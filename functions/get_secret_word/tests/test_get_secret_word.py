import sys, os
import pytest
import requests
import json

from .. import secret_word

filedir = os.path.dirname(__file__)
parentdir = os.path.dirname(filedir)

sys.path.append(sys.path.insert(0, filedir))

url = 'https://b578bine84.execute-api.us-east-1.amazonaws.com/dev/get_secret_word/'
with open(parentdir + '/fives.shuffled') as fh:
    words = [word.rstrip() for word in fh]


def test_getting_specific_word():
    index = 100
    word = words[index]

    response = requests.get(url + str(index))
    assert response.text == '{"index": 100, "word": "unsay"}'

def test_getting_random_word():
    response = requests.get(url)
    response.encoding = 'ISO-8859-1'
    data = json.loads(response.text)
    index = data["index"]
    print index
    assert words[int(index)] == data["word"]