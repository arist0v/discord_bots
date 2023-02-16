"""
bot.py
===================
This module contain bot for discord

@Author: Arist0v
"""
import discord
from random import randint


class Marvin(discord.Client):
    """
    This class represent the Marvin bot

    This bot, as marvin the android, is not really usefull
    """

    def __init__(self, token, intents=discord.Intents.default()):
        print("init Marvin")
        intents.message_content = True
        super().__init__(intents=intents)
        self.run(token)

    async def on_ready(self):
        print(f'{self.user} has connected to Discord')


    async def on_message(self, message):
        if message.author == self.user:
            return
        bot_actions = [self.__pi, self.__tp, self.__answer]

        for action in bot_actions:
            await action(message)

    async def __response(self, message, response):
            await message.channel.send(response)

    def __random_start(self, trigger = 1, max_range=5) -> bool:
        random_number = randint(1, max_range)
        return trigger == random_number

    async def __pi(self, message):
        response = "3.14159"
        splited_lower_message = message.content.lower().split(" ")
        triggers = ["pis", "pi"]
        for trigger in triggers:
            if trigger in splited_lower_message and self.__random_start():
                await self.__response(message, response)

    async def __tp(self, message):
        response = f"there you go {message.author.mention} :roll_of_paper:"
        splited_lower_message = message.content.lower().split(" ")
        triggers = ["tp", "tps"]
        for trigger in triggers:
            if trigger in splited_lower_message and self.__random_start():
                await self.__response(message, response)

    async def __answer(self, message):
        response = f"The only answer you need {message.author.mention} is 42!"
        triggers = ["?", "question", "questions"]
        splited_lower_message = message.content.lower().split(" ")
        should_response = False
        for trigger in triggers:
            if trigger in splited_lower_message:
                should_response = True
        for word in splited_lower_message:
            if "?" in word:
                should_response = True

        if should_response and self.__random_start():
            await self.__response(message, response)

