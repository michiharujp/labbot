# coding: utf-8

from slackbot.bot import respond_to
import random

@respond_to('dice')
def respond(message):
    roll = random.randint(1, 6)
    message.reply(':game_die: {}'.format(roll))
