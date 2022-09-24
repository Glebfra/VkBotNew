import vk_api

from src.VkBot import VkBot


def main():
    vk = vk_api.VkApi(token='123')
    vk_bot = VkBot(vk)


if __name__ == '__main__':
    main()
