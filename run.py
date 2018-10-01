# coding: utf-8

import six
from slackbot.bot import Bot, default_reply

@default_reply
def custom_default_handler(message):
    reply = [
        u'"{}"は知らないコマンドだワン！'
        u'使えるコマンドを見せるワン！\n'.format(message.body['text']),
    ]
    reply += [
        u'    • `{}`'.format(v.__doc__ or p.pattern) 
        for p, v in six.iteritems(message._plugins.commands['respond_to'])
    ]
    message.reply(u'\n'.join(reply))

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    print('start slackbot')
    main()
