# coding: utf-8

import random
from slackbot.bot import respond_to

def rank_text(items):
    msg = ''
    for i, item in enumerate(items, start=1):
        msg += "{}: {}\n".format(i,item)
    return msg

@respond_to(r'shuffle *(.*)')
def shuffle(message, items):
    """shuffle 要素1 要素2 要素3"""
    items = items.split()
    if len(items) < 2:
        message.send('要素を２つ以上にして、空白区切りで渡すワン！')
    else:
        random.shuffle(items)
        message.send(rank_text(items))
