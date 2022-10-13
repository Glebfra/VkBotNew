import vk_api
from vk_api.longpoll import VkLongPoll

from src.Messages import Messages
from src.additional import *


class VkBot(object):
    def __init__(self, vk):
        self.vk = vk
        self.longpool = VkLongPoll(self.vk, wait=25)
        self.vk_api = vk.get_api()

        self.ids = load_json_file('users')
        self.update_users()
        self.commands = load_json_file('commands')

        self.messages_threads = {user_id: Messages(self.vk_api, user_id, self.longpool) for user_id in
                                 self.ids['users']}

    @classmethod
    def create_bot(cls, token_file='token.txt'):
        with open(token_file, 'r') as file:
            token = file.read()
        vk = vk_api.VkApi(token=token)
        return cls(vk)

    def update_users(self):
        self.ids['users'] = self.vk_api.groups.getMembers(group_id=self.ids['group_id'])['items']
        update_json_file('users', self.ids)

    def message_logic(self):
        for event in messages_listener(self.longpool):
            request = event.text.lower()
            if request == 'начать':
                self.messages_threads[event.user_id].send_keyboard()
            elif request in self.commands:
                self.messages_threads[event.user_id].run_command(command=self.commands[request])
