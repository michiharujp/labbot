# coding: utf-8

from slackbot.bot import respond_to
import urllib.request
import urllib.parse

IMG_PATH = './src/tex.png'
API_URL = 'http://chart.apis.google.com/chart?cht=tx&chl='

def download(url, path):
    try:
        data = urllib.request.urlopen(url).read()
        with open(path, mode='wb') as f:
            f.write(data)
        return True
    except urllib.error.URLError as e:
        print(e)
        return False

@respond_to(r'tex *(.*)')
def tex_img_url(message, txt):
    """tex TeXソース"""
    txt = urllib.parse.quote(txt)
    img_url = API_URL + txt
    if download(img_url, IMG_PATH):
        message.channel.upload_file('tex', IMG_PATH)
    else:
        message.reply('形式が正しくないワン！')
