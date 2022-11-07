from vkbottle.bot import BotLabeler, Message
from .controllers import homework_controller

bl = BotLabeler()


@bl.message(text=['дз', 'домашка', 'Дз', 'Домашка'])
async def get_homework(message: Message):
    await homework_controller.get_homework(message)


@bl.message(text=homework_controller.homework.get_keys())
async def select_homework(message: Message):
    await homework_controller.select_homework(message)


@bl.message(text=['Добавить домашку', 'добавить домашку'])
async def add_homework(message: Message):
    await homework_controller.add_homework(message)
