from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from confbot import key_bot_api
import logging
import ephem


# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater(key_bot_api, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet(bot, update):
    user_text = update.message.text
    planet_name = user_text.split()
    print(planet_name)
    mars = ephem.Mars('2016/09/23')
    print(ephem.constellation(mars))
    update.message.reply_text(planet_name)
    update.message.reply_text(ephem.constellation(mars))


main()
