import random

import pytest

from python_tests_1.test_api_service.files_with_expected_responses.data import dogs_list


@pytest.fixture(scope="session")
def base_url():
    return "https://dog.ceo/api/"


# Не очень понимаю, как здесь определить фикстуру, тесты не проходят в таком варианте:
@pytest.fixture(scope="session")
def dogs_data():
    dogs_data = dogs_list
    return dogs_data


@pytest.fixture(scope="session")
def random_param(dogs_data):
    return random.choice(dogs_list)
