from __future__ import print_function
import sys, os
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../"))
sys.path.append(os.path.join(here, "../vendored"))

import json
import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)

from scorer import Scorer

def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))

    guess = event["pathGuess"]
    index = event["pathIndex"]

    score = Scorer()
    result = score.score_word(guess, int(index))
    return "score {}".format(result)
    return { "score": result }
