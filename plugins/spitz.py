# coding: utf-8

import urllib.request
from bs4 import BeautifulSoup
from slackbot.bot import respond_to
import random

def spitz_text():
    url = 'https://www.youtube.com/playlist?list=UUEAOVoVVtVBhcn7vLIQIkDA'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('a', attrs={ 'class': 'yt-uix-tile-link' })
    title = random.choice(tags)
    return '{} https://www.youtube.com{}'.format(title.contents[0].strip(), title.get('href'))

@respond_to('spitz')
def respond_func(message):
    message.reply(spitz_text())
