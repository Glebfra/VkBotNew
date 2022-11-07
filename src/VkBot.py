from vkbottle.bot import Bot

from routes import labelers
from src.additional import *


class VkBot(object):
    def __init__(self):
        self.bot = Bot(token=load_file('token.txt'))

        for custom_labeler in labelers:
            self.bot.labeler.load(custom_labeler)

    def run_bot(self):
        self.bot.run_forever()


if __name__ == '__main__':
    vkBot = VkBot()
    vkBot.run_bot()
