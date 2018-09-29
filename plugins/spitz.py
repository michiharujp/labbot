import urllib.request
import re
from bs4 import BeautifulSoup
from slackbot.bot import respond_to
import random

def spitz_text(url):
	html = urllib.request.urlopen(url)
	soup = BeautifulSoup(html, "html.parser")
	a_tag = soup.find('ul', attrs={'class' : 'yt-uix-shelfslider-list'})
	tags = a_tag.find_all(attrs ={'class' : 'yt-lockup-title'})
	array=[]
	for title in tags:
		array.append(title.find("a").contents[0]+","+"https://www.youtube.com/"+title.a.get("href"))
	return array

@respond_to('スピッツ')

def respond_func(message):
    url="https://www.youtube.com/channel/UCEAOVoVVtVBhcn7vLIQIkDA"
    message.reply(random.choice(spitz_text(url)))
