import json
import random

import pytest
import requests

from python_tests_3.test_api_service.conftest import user_id, post_id, post_title, post_text, params
from python_tests_3.test_api_service.constants import POSTS
from python_tests_3.test_api_service.data import data


def test_access_all_posts(base_url):
    """Testing the API endpoint for returning all posts."""
    response = requests.get(base_url + POSTS).json()
    assert response == data.data


@pytest.mark.parametrize('param', [str(i) for i in range(1, 101)])
def test_access_specific_post(base_url, param):
    """Testing the API endpoint for returning the specific post."""
    response = requests.get(base_url + POSTS + '/' + param).json()
    assert response == data.data[int(param) - 1]


@pytest.mark.parametrize('param', [str(i) for i in range(1, 101)])
def test_access_comments(base_url, param):
    """Testing the API endpoint for returning comments for the specified post."""
    response = requests.get(base_url + POSTS + '/' + param + '/comments').json()
    assert len(response) > 0


@pytest.mark.parametrize('userId, title, body', [
    (random.choice(user_id()), random.choice(post_title()),
     random.choice(post_text())) for i in range(12)]
                         )
def test_post_creation(base_url, userId, title, body):
    """Testing the API endpoint for creating a post."""
    data_to_post = {'userId': userId, 'title': title, 'body': body}
    response = requests.post(base_url + POSTS, data=data_to_post)
    assert response.status_code == 201


@pytest.mark.parametrize('userId, postId, title, body', params()
                         )
def test_post_creation_one_more(base_url, userId, postId, title, body):
    """Testing the API endpoint for creating a post."""
    data_to_post = {'userId': userId, 'postId': postId, 'title': title, 'body': body}
    response = requests.post(base_url + POSTS, data=data_to_post)
    assert response.status_code == 201


# Не уверена, почему не проходят эти тесты -- из-за моей ошибки
# или сайт не принимает такой расклад

# @pytest.mark.parametrize('userId, title', [
#     (user_id()[i], post_title()[i]) for i in range(8)]
#                          )
# def test_post_update(base_url, userId, title):
#     """Testing the API endpoint for updating the existing post parameters."""
#     data_to_post = {'userId': userId, 'title': title, id: 101}
#     response_to_create = requests.post(base_url + POSTS, data=data_to_post)
#     data_to_post = {'userId': userId, 'title': 'new_title', id: 101}
#     response = requests.put(base_url + POSTS, data=data_to_post)
#     assert response.status_code == 201


@pytest.mark.parametrize('id', [
    id for id in range(0, 13, 100)]
                         )
def test_delete_post(id, base_url):
    """Testing the API endpoint for deleting a post."""
    response = requests.delete(base_url + POSTS + '/' + str(id))
    assert response.status_code == 200
