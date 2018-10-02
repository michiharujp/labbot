# coding: utf-8

import urllib.request
from bs4 import BeautifulSoup
from slackbot.bot import respond_to
import random

def spitz_text():
    url = 'https://www.youtube.com/channel/UCEAOVoVVtVBhcn7vLIQIkDA'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    a_tag = soup.find('ul', attrs={ 'class': 'yt-uix-shelfslider-list' })
    tags = a_tag.find_all(attrs={ 'class': 'yt-lockup-title' })
    array = []
    for title in tags:
        array.append('{} https://www.youtube.com/{}'.format(title.find('a').contents[0], title.a.get('href')))
    return array

@respond_to('spitz')
def respond_func(message):
    message.reply(random.choice(spitz_text()))
