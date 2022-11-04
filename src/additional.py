import json
from datetime import datetime
from threading import Thread

from vk_api.longpoll import VkEventType


def load_json_file(filename: str) -> json:
    try:
        with open(f'json/{filename}.json', 'r') as file:
            return json.load(file)

    except:
        return None


def update_json_file(filename: str, dictionary: dict) -> bool:
    try:
        with open(f'json/{filename}.json', 'w') as file:
            json.dump(dictionary, file)
        return True

    except:
        return False


def add_dict(filename: str, key: str, value: str) -> bool:
    """
    This function adds the value to json file and updates it

    :param filename: Filename
    :param key: key value of dictionary
    :param value: value of dictionary
    :return: boolean value (True) if everything's right (False) if not
    """
    try:
        dictionary = load_json_file(filename)
        dictionary[key] = value
        update_json_file(filename, dictionary)
        return True

    except:
        return False


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
