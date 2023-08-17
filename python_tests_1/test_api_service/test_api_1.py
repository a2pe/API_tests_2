import random

import pytest
import requests

from files_with_expected_responses import data
from python_tests_1.test_api_service.constants import OK, BREED, BREEDS, IMAGE, IMAGES, ALL_LIST, RANDOM
from python_tests_1.test_api_service.files_with_expected_responses.data import dogs_list


@pytest.mark.smoke
def test_list_all_breeds_status_code(base_url):
    """Testing the API endpoint for returning 200-OK status code for listing all breeds"""
    assert requests.get(base_url + BREEDS + ALL_LIST).status_code == 200


@pytest.mark.smoke
def test_list_all_breeds(base_url):
    """Testing the API endpoint for returning all breeds as listed in the file."""
    assert requests.get(base_url + BREEDS + ALL_LIST).json() == data.data


@pytest.mark.smoke
def test_get_random_image_status_code(base_url):
    """Testing the API endpoint for returning a random image."""
    assert requests.get(base_url + BREEDS + IMAGE + RANDOM).status_code == 200


@pytest.mark.smoke
def test_get_random_image(base_url):
    """Testing the API endpoint for returning a random image."""
    response = requests.get(base_url + BREEDS + IMAGE + RANDOM).json()
    assert response['status'] == OK


@pytest.mark.parametrize('param', [str(i) for i in [0, 1, 49, 50]])
def test_get_multiple_random_images(base_url, param):
    """Testing the API endpoint for returning multiple random images."""
    response = requests.get(base_url + BREEDS + IMAGE + RANDOM + param).json()
    assert response['status'] == OK


# Using parametrization for returning the random breed
@pytest.mark.parametrize('param', [str(random.choice(dogs_list))])
def test_get_breed_images(base_url, param):
    """Testing the API endpoint for returning all images for the specific breed"""
    assert requests.get(base_url + BREED + param + IMAGES).status_code == 200


# Using the pytest fixture to return the random breed
def test_get_breed_images_w_fixture(base_url, random_param):
    """Testing the API endpoint for returning all images for the specific breed."""
    response = requests.get(base_url + BREED + random_param + IMAGES).json()
    assert response['status'] == OK


def test_get_random_breed_images(base_url, random_param):
    """Testing the API endpoint for returning a random image for the specific breed."""
    response = requests.get(base_url + BREED + random_param + IMAGES + RANDOM).json()
    assert response['status'] == OK


@pytest.mark.parametrize('param', [str(i) for i in [1, 15]])
def test_api_by_random_breed_images(base_url, random_param, param):
    """Testing the API endpoint for returning several random images for the specific breed."""
    response = requests.get(base_url + BREED + random_param + IMAGES + RANDOM + param).json()
    assert len(response['message']) == int(param)


@pytest.mark.parametrize('param', [pytest.param(str(i), marks=pytest.mark.xfail(reason="Jira-1234"))
                                   for i in (0, 1000000000)]
                         )
def test_api_random_image_zero(base_url, param, random_param):
    """Testing the API endpoint for returning a random image for the specific breed with 0 and maximum values."""
    response = requests.get(base_url + BREEDS + random_param + IMAGES + RANDOM + param)
    assert response.status_code != 200
    assert 'message' in response.json()
    assert len(response.json()['message']) == int(param)
