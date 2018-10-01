# coding: utf-8

import requests
from bs4 import BeautifulSoup
from slackbot.bot import respond_to

def make_soup_from(url):
    re = requests.get(url)
    html = re.text
    soup = BeautifulSoup(html, "html.parser")
    return soup

def translate_from_weblio(word):
    url = "https://ejje.weblio.jp/content/{}".format(word)
    soup = make_soup_from(url)
    explain = soup.find("td", {"class":"content-explanation ej"})
    if explain == None:
        return None
    else:
        return explain.string

@respond_to("dict +(.+)")
def respond_word(message, word):
    """dict 英単語"""
    if translate_from_weblio(word) == None:
        message.reply("見つからなかったワン！")
    else:
        message.reply(translate_from_weblio(word) + "、 だワン！")
