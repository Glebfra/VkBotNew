import random

from src.additional import *


class Messages(object):
    def __init__(self, vk_api, user_id):
        self.user_id = user_id
        self.vk_api = vk_api

        self.urls = load_json_file('urls')
        self.messages = load_json_file('messages')

        self.start_week = datetime(2022, 9, 1).isocalendar()[1]

    @logging
    def run_command(self, command: str):
        exec(f'self.command_{command}()')
        return f'User {self.user_id} used command {command}'

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
        message = ''
        for subject in homework:
            message += f'-- {subject} -- задано: \n' \
                       f'{homework[subject]}\n' \
                       f'\n'
        self.send_message(message)

    def command_birthday(self):
        self.send_message(self.messages['birthday'], attachment=self.urls['birthday'])

    def command_set_base(self):
        self.send_message(self.messages['set_base'])

    def command_get_base(self):
        pass
