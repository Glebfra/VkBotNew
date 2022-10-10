from src.VkBot import VkBot


def main():
    vk_bot = VkBot.create_bot()
    vk_bot.message_logic()


if __name__ == '__main__':
    main()
