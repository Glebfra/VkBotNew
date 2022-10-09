import json

from vk_api.longpoll import VkLongPoll, VkEventType

from src.Messages import Messages


class VkBot(object):
    def __init__(self, vk):
        self.vk = vk
        self.longpool = VkLongPoll(self.vk)
        self.vk_api = vk.get_api()

        self.user_thread = []

        # Downloading the users
        with open('json/users.json', 'r') as file:
            self.ids = json.load(file)
        self.messages_threads = {user_id: Messages(self.vk_api, user_id) for user_id in self.ids['users']}

        # Downloading the commands
        with open('json/commands.json') as file:
            self.commands = json.load(file)

    def messages_logic(self, event):
        pass

    def message_loop(self):
        for event in self._messages_listener():
            self.messages_logic(event)

    def _messages_listener(self):
        for event in self.longpool.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                yield event
