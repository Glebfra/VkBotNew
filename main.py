import vk_api

from src.VkBot import VkBot


def main():
    with open('token.txt', 'r') as file:
        token = file.read()
    vk = vk_api.VkApi(token=token)
    vk_bot = VkBot(vk)
    vk_bot.message_loop()


if __name__ == '__main__':
    main()
