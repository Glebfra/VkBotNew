import random

from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from src.additional import load_json_file


class Keyboard(object):
    def __init__(self, vk_api, user_id):
        self.vk_api = vk_api
        self.user_id = user_id

        self.keyboard = None
        self.homework_keyboard = None
        self.create_homework_keyboard = None

        self.init_keyboard()
        self.init_homework_keyboard()
        self.init_create_homework_keyboard()

    def send_keyboard(self, message: str = 'Обращайся ко мне еще :-)'):
        self.vk_api.messages.send(
            user_id=self.user_id,
            random_id=random.randint(-1024, 1024),
            keyboard=self.keyboard.get_keyboard(),
            message=message
        )

    def send_homework_keyboard(self, message: str = 'Выбери домашку, которую хочешь просмотреть'):
        self.vk_api.messages.send(
            user_id=self.user_id,
            random_id=random.randint(-1024, 1024),
            keyboard=self.homework_keyboard.get_keyboard(),
            message=message
        )

    def send_create_homework_keyboard(self, message: str = 'Выбери домашку, которую хочешь добавить или нажми кнопку добавить, чтобы добавить новый предмет'):
        self.vk_api.messages.send(
            user_id=self.user_id,
            random_id=random.randint(-1024, 1024),
            keyboard=self.create_homework_keyboard.get_keyboard(),
            message=message
        )

    def init_keyboard(self):
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Расписание', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Неделя', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Домашка', color=VkKeyboardColor.PRIMARY)

        keyboard.add_line()

        keyboard.add_button('Др', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Выдать базу', color=VkKeyboardColor.SECONDARY)
        keyboard.add_button('Новая база', color=VkKeyboardColor.SECONDARY)

        keyboard.add_line()

        keyboard.add_button('Добавить домашку', color=VkKeyboardColor.NEGATIVE)

        self.keyboard = keyboard

    def init_homework_keyboard(self):
        keyboard = VkKeyboard(one_time=True)
        homework = load_json_file('homework')

        iteration = 1
        for subject in homework:
            keyboard.add_button(f'{subject}', color=VkKeyboardColor.SECONDARY)
            if not iteration % 3:
                keyboard.add_line()
            iteration += 1

        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.PRIMARY)

        self.homework_keyboard = keyboard

    def init_create_homework_keyboard(self):
        keyboard = VkKeyboard(one_time=True)
        homework = load_json_file('homework')

        iteration = 1
        for subject in homework:
            keyboard.add_button(f'{subject}', color=VkKeyboardColor.SECONDARY)
            if not iteration % 3:
                keyboard.add_line()
            iteration += 1

        keyboard.add_line()
        keyboard.add_button('Добавить предмет', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.PRIMARY)

        self.create_homework_keyboard = keyboard
