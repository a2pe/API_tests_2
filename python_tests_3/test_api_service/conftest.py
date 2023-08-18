import pytest
import string
import random

from allpairspy import AllPairs


@pytest.fixture
def base_url():
    return 'https://jsonplaceholder.typicode.com'


def user_id():
    user_ids = [-1, 0, 1, 1000000]
    numeric_ids = [random.randint(0, 1000) for i in range(2)]
    alphabetic_ids = [''.join(random.choices(string.ascii_lowercase, k=7)) for item in range(2)]
    user_ids.extend(numeric_ids)
    user_ids.extend(alphabetic_ids)
    return user_ids


def post_id():
    post_ids = [0, 1, 1000000, -1]
    numeric_ids = [random.randint(0, 100000) for i in range(2)]
    alphabetic_ids = [''.join(random.choices(string.ascii_lowercase, k=7)) for item in range(2)]
    post_ids.extend(numeric_ids)
    post_ids.extend(alphabetic_ids)
    return post_ids


def post_title():
    post_titles = ['', ' ', '1a234 Hnd ', ' 1 fff']
    alphabetic_titles = [''.join(random.choices(string.ascii_lowercase, k=7)) for item in range(4)]
    post_titles.extend(alphabetic_titles)
    return post_titles


def post_text():
    post_texts = ['', ' ', '1a234 Hnd ', ' 1 fff', '123']
    alphabetic_texts = [''.join(random.choices(string.ascii_lowercase, k=15)) for item in range(3)]
    post_texts.extend(alphabetic_texts)
    return post_texts


def params():
    parameters = (user_id(), post_id(), post_title(), post_text())
    param_pairs = []
    for i, pairs in enumerate(AllPairs(parameters)):
        param_pairs.append(tuple(pairs))
    return param_pairs
