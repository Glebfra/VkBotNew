import random

from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from src.additional import load_json_file


class Keyboard(object):
    def __init__(self, vk_api, user_id):
        self.vk = vk_api
        self.user_id = user_id
        self.keyboard = VkKeyboard(one_time=False)
        self.special_ids = load_json_file('users')['special_users']

        if user_id in self.special_ids:
            self.create_special_keyboard()
        else:
            self.create_keyboard()

    def send_keyboard(self):
        self.vk.messages.send(
            user_id=self.user_id,
            random_id=random.randint(-1024, 1024),
            keyboard=self.keyboard.get_keyboard(),
            message='Клавиатура снизу :-)'
        )

    def create_keyboard(self):
        self.keyboard.add_button('Расписание', color=VkKeyboardColor.PRIMARY)
        self.keyboard.add_button('Неделя', color=VkKeyboardColor.PRIMARY)
        self.keyboard.add_button('Домашка', color=VkKeyboardColor.PRIMARY)

        self.keyboard.add_line()

        self.keyboard.add_button('Др', color=VkKeyboardColor.POSITIVE)
        self.keyboard.add_button('Выдать базу', color=VkKeyboardColor.SECONDARY)
        self.keyboard.add_button('Новая база', color=VkKeyboardColor.SECONDARY)

    def create_special_keyboard(self):
        self.create_keyboard()

        self.keyboard.add_line()

        self.keyboard.add_button('Добавить домашку', color=VkKeyboardColor.NEGATIVE)
