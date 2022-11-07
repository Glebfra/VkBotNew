from vkbottle.bot import Message

from .AbstractController import AbstractController


class HomeworkController(AbstractController):
    def __init__(self):
        super().__init__()
        self.homework = self.get_json_file('homework')

    async def get_homework(self, message: Message, subject=None):
        response = f'-- {subject} --\n' \
                   f'{self.homework[subject]}\n\n'
        await message.answer(response)

    async def select_homework(self, message: Message):
        pass

    async def add_homework(self, message: Message):
        await message.answer('Метод добавления домашки')

    def get_file(self, filename):
        return super(HomeworkController, self).get_file(filename)

    def get_json_file(self, filename):
        return super(HomeworkController, self).get_json_file(filename)

    def update_json_file(self, filename: str, dictionary: dict) -> None:
        super(HomeworkController, self).update_json_file(filename, dictionary)
