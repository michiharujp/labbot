# coding: utf-8

from slackbot.bot import respond_to
import random

@respond_to(r'(?:([0-9]+)面)?(?:さいころ|サイコロ|ダイス)')
def respond_n(message, n):
    n = 6 if n is None or int(n) < 1 else int(n)
    roll = random.randint(1, n)
    message.reply(':game_die: {}'.format(roll))
