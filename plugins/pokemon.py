# coding: utf-8

import urllib.request
import re
from bs4 import BeautifulSoup
from slackbot.bot import respond_to
import random

def pokemon_text(url):

    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    name = soup.title.string
    name = name[:name.find("｜")]

    height = soup.table.find("td",text=re.compile("\dm")).string
    weight = soup.table.find("li",text=re.compile("\dkg")).string

    text = name + "の高さは" + height + "で重さは" + weight + "です"
    return text

@respond_to('ポケモン')
def respond_func(message):
    pokemon_number = random.randint(1,807)
    url = "https://yakkun.com/sm/zukan/n" + str(pokemon_number)
    img = "https://img.yakkun.com/poke/sm/n" + str(pokemon_number) + ".gif"
    message.send(pokemon_text(url) + img)
