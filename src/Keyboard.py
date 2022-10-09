from vk_api.keyboard import VkKeyboard, VkKeyboardColor


class Keyboard(object):
    def __init__(self, vk_api, user_id):
        self.vk = vk_api
        self.user_id = user_id
        self.keyboard = VkKeyboard(one_time=False)

    def send_keyboard(self):
        self.vk.messages.send()
