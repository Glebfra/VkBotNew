from vkbottle.bot import Message

from .AbstractController import AbstractController


class HomeworkController(AbstractController):
    def __init__(self):
        super().__init__()

    async def get_homework(self, message: Message, subject=None):
        homework = self.get_json_file('homework')

        response = ''
        for subject in homework:
            response += f'-- {subject} --\n' \
                        f'{homework[subject]}\n\n'
        await message.answer(response)

    async def add_homework(self, message: Message, subject=None):
        await message.answer('Метод добавления домашки')

    def get_file(self, filename):
        return super(HomeworkController, self).get_file(filename)

    def get_json_file(self, filename):
        return super(HomeworkController, self).get_json_file(filename)

    def update_json_file(self, filename: str, dictionary: dict) -> None:
        super(HomeworkController, self).update_json_file(filename, dictionary)
