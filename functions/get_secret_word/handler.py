from __future__ import print_function
import sys, os

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../"))
sys.path.append(os.path.join(here, "../vendored"))

import json
import logging

from secret_word import SecretWord

log = logging.getLogger()
log.setLevel(logging.DEBUG)

def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))
    secret_word = SecretWord(event)
    return { 'word': secret_word.word, 'index': secret_word.index }
