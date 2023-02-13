import sys

import discord_bot.pkg.bot as bots

from discord_bot.pkg.config import Config

if __name__ == '__main__':
    #  TODO create a class to init multiple bot by passing ini file
    ini_file = "./test.ini"
    config = Config(ini_file)
    if len(config.bots_list) == 0:
        print(f"No bot configuration present in {ini_file}")
        sys.exit(3)
    for bot in config.bots_list:
        try:
            bot_class = getattr(bots, bot[0].title())
        except AttributeError:
            print(f"bot class: {bot[0].title()} did not exsit")
            sys.exit(1)
        for token in bot[1]:
            bot_class(token)
