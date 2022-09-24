import json
import random

from datetime import datetime


class Messages(object):
    def __init__(self, vk_api, user_id):
        self.user_id = user_id
        self.vk_api = vk_api
        self.random_id = random.randint(-1024, 1024)

        self.urls = self._get_urls()
        self.messages = self._get_messages()

        self.start_week = datetime(2022, 9, 1).isocalendar()[1]

    def run_command(self, command: str, *args, **kwargs) -> None:
        """
        Method which select the command method

        :param command: Command
        :param args: positional arguments
        :param kwargs: key arguments
        """
        try:
            eval(f'self.command_{command}(*{args}, **{kwargs})')
        except AttributeError:
            raise AttributeError(f'You do not have these attributes {args}, {kwargs} on this function'
                                 f'self.command_{command}')

    def send_message(self, message: str, attachment: str = None) -> None:
        """
        Method which send message

        :param message: Message
        :param attachment: Attachment
        :return:
        """
        self.vk_api.messages.send(
            user_id=self.user_id,
            message=message,
            random_id=self.random_id,
            attachment=attachment
        )

    def command_schedule(self):
        """ Command schedule """
        self.send_message(self.messages['schedule'], self.urls['schedule'])

    def command_week(self):
        """ Command week """
        self.send_message(self.messages['week'] + f'{datetime.now().isocalendar()[1] - self.start_week + 1}')

    @staticmethod
    def _get_urls():
        with open('json/urls.json') as file:
            return json.load(file)

    @staticmethod
    def _get_messages():
        with open('json/messages.json') as file:
            return json.load(file)
