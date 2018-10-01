# coding: utf-8
import os
import json
import requests
import random
from slackbot.bot import respond_to

API_TOKEN = os.environ.get('SLACK_API_KEY')
BOT_ID = os.environ.get('BOT_ID')
SLACK_API_BASE = 'https://slack.com/api'

def get_user_ids(channel_id):
    query = { 'token': API_TOKEN, 'channel': channel_id }
    channel_url = SLACK_API_BASE + '/channels.info'

    r = requests.get(channel_url, params=query)
    data = json.loads(r.text)
    return data['channel']['members']

def get_users(ids):
    user_url = SLACK_API_BASE + '/users.info'
    # 全メンバーを格納する
    users = []
    for user_id in ids:
        if user_id == BOT_ID:
            continue

        query = { 'token': API_TOKEN, 'user': user_id }
        r = requests.get(user_url, params=query)
        data = json.loads(r.text)
        name = data['user']['profile']['display_name']
        if not name:
            name = data['user']['profile']['real_name']

        users.append(name)
    return users

def rank_text(users):
    msg = ''
    for i, user in enumerate(users, start=1):
        msg += "{}: {}\n".format(i,user)
    return msg


@respond_to('shuffle')
def shuffled_members(message):
    channel_id = message.channel._body['id']
    users = get_users(get_user_ids(channel_id))
    random.shuffle(users)
    message.send(rank_text(users))
