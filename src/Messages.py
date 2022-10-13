import random

from src.Keyboard import Keyboard
from src.additional import *


class Messages(Keyboard):
    def __init__(self, vk_api, user_id, longpool):
        super().__init__(vk_api, user_id)

        self.user_id = user_id
        self.vk_api = vk_api
        self.longpool = longpool

        self.urls = load_json_file('urls')
        self.messages = load_json_file('messages')

        self.start_week = datetime(2022, 9, 1).isocalendar()[1]

    @parallel
    def run_command(self, command: str, *args, **kwargs):
        exec(f'self.command_{command}(*{args}, **{kwargs})')
        self.send_keyboard()

    def send_message(self, message: str, attachment: str = None):
        self.vk_api.messages.send(
            user_id=self.user_id,
            message=message,
            random_id=random.randint(-1024, 1024),
            attachment=attachment
        )

    def command_start(self):
        self.send_message(self.messages['start'])

    def command_week(self):
        week = datetime.now().isocalendar()[1]
        self.send_message(f'{self.messages["week"]} {week - self.start_week + 1} неделя.')

    def command_schedule(self):
        self.send_message(self.messages['schedule'], attachment=self.urls['schedule'])

    def command_homework(self):
        homework = load_json_file('homework')
        self.init_homework_keyboard()
        self.send_homework_keyboard(self.messages['get_homework_1'])

    def command_create_homework(self):
        homework = load_json_file('homework')
        self.init_create_homework_keyboard()
        self.send_create_homework_keyboard(self.messages['create_homework_1'])

    def command_birthday(self):
        self.send_message(self.messages['birthday'], attachment=self.urls['birthday'])

    def command_set_base(self):
        self.send_message(self.messages['set_base'])

    def command_get_base(self):
        base = load_json_file('based')
        self.send_message(f"{self.messages['get_base']}"
                          f"{base[str(random.randint(0, len(base)-1))]}")
