from __future__ import print_function

import json
import logging
from random import randint

log = logging.getLogger()
log.setLevel(logging.DEBUG)

def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))
    words = load_dictionary()
    if 'pathIndex' in event:
        index = int(event['pathIndex'])
    else:
        index = randint(0, len(words) - 1)
    return words[index]

def load_dictionary():
    with open('lib/fives.shuffled') as fh:
        words = fh.readlines()
    return words    
