import json
from datetime import datetime
from threading import Thread


def load_json_file(filename):
    with open(f'json/{filename}.json', 'r') as file:
        return json.load(file)


def add_dict(filename, key, value):
    with open(f'json/{filename}.json', 'r') as file:
        dictionary = json.load(file)

    dictionary[key] = value

    with open(f'json/{filename}.json', 'w') as file:
        json.dump(dictionary, file)


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
