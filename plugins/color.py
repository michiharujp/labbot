# coding: utf-8

import os
import hashlib
from slackbot.bot import respond_to

@respond_to('color')
def random_color(message):
    color_code = '#' + hashlib.md5(os.urandom(64)).hexdigest()[:6]
    message.reply(color_code)
