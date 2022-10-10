import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from src.Keyboard import Keyboard
from src.Messages import Messages
from src.additional import load_json_file


class VkBot(object):
    def __init__(self, vk):
        self.vk = vk
        self.longpool = VkLongPoll(self.vk, wait=25)
        self.vk_api = vk.get_api()

        self.ids = load_json_file('users')
        self.commands = load_json_file('commands')

        self.messages_threads = {user_id: Messages(self.vk_api, user_id) for user_id in self.ids['users']}
        self.keyboard_threads = {user_id: Keyboard(self.vk_api, user_id) for user_id in self.ids['users']}

    @classmethod
    def create_bot(cls, token_file='token.txt'):
        with open(token_file, 'r') as file:
            token = file.read()
        vk = vk_api.VkApi(token=token)
        return cls(vk)

    def message_logic(self):
        for event in self._messages_listener():
            request = event.text.lower()
            if request == 'начать':
                self.keyboard_threads[event.user_id].send_keyboard()
            elif request in self.commands:
                self.messages_threads[event.user_id].run_command(command=self.commands[request])

    def _messages_listener(self):
        for event in self.longpool.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                yield event
