import random

import pytest

from python_tests_1.test_api_service.files_with_expected_responses.data import dogs_list


@pytest.fixture(scope="session")
def base_url():
    return "https://dog.ceo/api/"


@pytest.fixture
def random_param():
    return random.choice(dogs_list)
