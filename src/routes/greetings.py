from vkbottle.bot import BotLabeler, Message

bl = BotLabeler()


@bl.message(text=['привет', 'хай', 'здравствуй', 'начать', 'hi', 'start',
                  'Привет', 'Хай', 'Здравствуй', 'Начать', 'Hi', 'Start'])
async def greeting(message: Message):
    await message.answer(f'Привет мой друг {message.from_id}')
