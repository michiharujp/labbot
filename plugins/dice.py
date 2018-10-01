# coding: utf-8

from slackbot.bot import respond_to
import random

@respond_to(r'dice *([0-9]+)?')
def respond(message, n):
    """dice [面の数]"""

    if n is None:
        n = 6
    elif int(n) < 2:
        message.reply('サイコロは2面以上にしないと意味がないワン！')
        return
    else:
        n = int(n)

    roll = random.randint(1, n)
    message.reply(':game_die: {}'.format(roll))
