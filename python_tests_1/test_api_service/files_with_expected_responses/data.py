import json

import os

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


JSON_FILE_PATH = get_path(filename="all_breeds.json")

with open(JSON_FILE_PATH, 'r') as file:
    data = json.load(file)
    dogs = data['message']
    dogs_list = [i for i in dogs]
    hounds = data['message']['hound']
