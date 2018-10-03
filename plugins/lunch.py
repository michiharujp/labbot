# coding: utf-8

import json
import os
import random
from slackbot.bot import respond_to
from urllib.request import urlopen

API_KEY = os.environ.get('HOTPEPPER_API_KEY')
LATITUDE = os.environ.get('LATITUDE')
LONGITUDE = os.environ.get('LONGITUDE')

@respond_to('lunch')
def respond(message):
    url = 'https://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key={}' \
    '&format=json&count=100' \
    '&lat={}&lng={}&order=4&lunch=1'.format(API_KEY, LATITUDE, LONGITUDE)

    r = json.loads(urlopen(url).read().decode('utf8'))
    shop = random.choice(r['results']['shop'])

    message.reply('{} {}'.format(shop['name'], shop['urls']['pc']))
