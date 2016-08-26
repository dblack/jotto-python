import sys, os
import pytest
import requests
import json
from mock import patch, mock_open

from .. import guess
dictionary = ['horst', 'pause', 'corse', 'moule', 'smuse', 'moose', 
               'input', 'strip', 'misty']
matches = ['horst', 'pause', 'corse', 'moule', 'smuse', 'moose']

filedir = os.path.dirname(__file__)
parentdir = os.path.dirname(filedir)

sys.path.append(sys.path.insert(0, filedir))

url = 'https://b578bine84.execute-api.us-east-1.amazonaws.com/dblack/guess_humans_word/'

def test_loads_filtered_dictionary():
    with patch('__builtin__.open', mock_open(read_data = '\n'.join(dictionary))) as mock_file:
        g = guess.Guess('house3')
        assert g.load_filtered_dictionary() == matches

def test_gets_first_guess():
    response = requests.get(url)
    print response.text