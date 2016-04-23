from __future__ import print_function

import json
import logging

import os

from secret_word import SecretWord

log = logging.getLogger()
log.setLevel(logging.DEBUG)

def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))
    return SecretWord(event).get()