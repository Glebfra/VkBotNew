import json
from datetime import datetime
from threading import Thread

from vk_api.longpoll import VkEventType


def load_json_file(filename: str):
    with open(f'../json/{filename}.json', 'r') as file:
        return json.load(file)


def update_json_file(filename: str, dictionary: dict):
    with open(f'../json/{filename}.json', 'w') as file:
        json.dump(dictionary, file)


def add_dict(filename: str, key: str, value: str):
    with open(f'../json/{filename}.json', 'r') as file:
        dictionary = json.load(file)

    dictionary[key] = value

    with open(f'../json/{filename}.json', 'w') as file:
        json.dump(dictionary, file)


def load_file(filename: str):
    try:
        with open(f'../{filename}', 'r') as file:
            response = file.read()
        return response
    except FileNotFoundError:
        raise FileNotFoundError


def parallel(func):
    def inner(*args, **kwargs):
        th = Thread(target=func, args=args, kwargs=kwargs)
        th.start()

    return inner


def logging(func):
    def inner(*args, **kwargs):
        log = func(*args, **kwargs)
        time = datetime.now().ctime()
        with open('log/log.txt', 'a') as file:
            file.write(f'{time}: {log}\n')

    return inner


def append_dict(filename: str, key: str, value: str):
    homework = load_json_file(filename)
    homework[key].append(value)


def messages_listener(longpool):
    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            yield event
