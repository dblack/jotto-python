import sys, os
import pytest
import requests
import json

from .. import scorer

filedir = os.path.dirname(__file__)
parentdir = os.path.dirname(filedir)

sys.path.append(sys.path.insert(0, filedir))
url = 'https://b578bine84.execute-api.us-east-1.amazonaws.com/dev/score_humans_guess/'

def test_get_score():
    request_url = "{}{}/{}".format(url, 'unsay', str(100))
    response = requests.get(request_url)

    assert response.text == '{"score": 5}'

    request_url = "{}{}/{}".format(url, 'horse', str(8193))
    response = requests.get(request_url)

    assert response.text == '{"score": 4}'
