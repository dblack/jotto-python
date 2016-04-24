from __future__ import print_function

import json
import logging

import guess

log = logging.getLogger()
log.setLevel(logging.DEBUG)

def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))
    history_string = event["pathHistory"]
    a_guess = guess.Guess(history_string)
    return { "guess": a_guess.make_guess() }