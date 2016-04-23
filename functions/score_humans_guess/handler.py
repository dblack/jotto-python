from __future__ import print_function

import json
import logging

from scorer import Scorer

log = logging.getLogger()
log.setLevel(logging.DEBUG)

def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))

    guess = event["pathGuess"]
    index = event["pathIndex"]

    score = Scorer()
    result = score.score_word(guess, int(index))
    return { "score": result }
