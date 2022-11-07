from abc import ABC, abstractmethod

from src.additional import *


class AbstractController(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_file(self, filename: str):
        with open(f'../{filename}', 'r') as file:
            return file.read()

    @abstractmethod
    def get_json_file(self, filename: str):
        with open(f'../json/{filename}.json', 'r') as file:
            return json.load(file)

    @abstractmethod
    def update_json_file(self, filename: str, dictionary: dict) -> None:
        with open(f'../json/{filename}.json', 'w') as file:
            json.dump(dictionary, file)
