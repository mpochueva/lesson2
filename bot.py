from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from confbot import key_bot_api
import logging
import ephem
from datetime import datetime


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
    dp.add_handler(CommandHandler("planet", get_constellation))
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


def get_planet_list():
    planet_list = []
    for pnum, ptype, pname in ephem._libastro.builtin_planets():
        if ptype == "Planet":
            planet_list.append(pname)
    print(planet_list)
    return planet_list


def get_constellation(bot, update):
    planet_list = get_planet_list()
    user_text = update.message.text
    now = datetime.strftime(datetime.now(), "%Y/%m/%d")
    planet_name = user_text.split()[1].capitalize()
    if planet_name in planet_list:
        print(now)
        print(planet_name)
        constellation = getattr(ephem, planet_name)(now)
        print(ephem.constellation(constellation))
        update.message.reply_text(planet_name)
        update.message.reply_text("Planet " + planet_name + " is in the " +
                                  ephem.constellation(constellation)[1] + " constellation today")
    else:
        update.message.reply_text("The name entered is not a planet name. Please try again "
                                  "using the names from the list: {}".format(', '.join(planet_list)))


main()
