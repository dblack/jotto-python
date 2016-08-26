from __future__ import print_function
import sys, os
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../"))
sys.path.append(os.path.join(here, "../vendored"))
sys.path.append(os.path.join(here, "./vendored"))

import json
import logging

import guess

log = logging.getLogger()
log.setLevel(logging.DEBUG)

def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))
    history_string = event.get("pathHistory", "")
    a_guess = guess.Guess(history_string)
    log.debug('Computer is guessing: {}'.format(a_guess.guessed_word))
    return { "guess": a_guess.make_guess() }
