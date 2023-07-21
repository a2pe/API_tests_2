import pytest
import requests
import random


@pytest.fixture(scope="session")
def base_url():
    return 'https://api.openbrewerydb.org/v1/breweries'


# Не очень понимаю, почему здесь фикстура не принимается - ошибка "No schema supplied"
def get_breweries(base_url_2='https://api.openbrewerydb.org/v1/breweries'):
    response = requests.get(base_url_2).json()
    brewery_ids = [response[i]['id'] for i in range(len(response))]
    return brewery_ids


@pytest.fixture(scope="session")
def single_brewery():
    random_brewery = random.choice(get_breweries())
    return random_brewery


def get_brewery_cities(base_url_2='https://api.openbrewerydb.org/v1/breweries'):
    response = requests.get(base_url_2).json()
    brewery_cities = [response[i]['city'] for i in range(len(response))]
    return brewery_cities


@pytest.fixture(scope="session")
def brewery_city():
    brewery_city = random.choice(get_brewery_cities())
    return brewery_city


def get_several_brewery_ids():
    several_brewery_ids = [random.choice(get_breweries()) for i in range(1, random.randint(2, 10))]
    return several_brewery_ids


def brewery_types():
    types = {'micro': 'Most craft breweries. For example, Samual Adams is still considered a micro brewery.',
             'nano': 'An extremely small brewery which typically only distributes locally',
             'regional': 'A regional location of an expanded brewery. Ex. Sierra Nevada’s Asheville, NC location',
             'brewpub': 'A beer-focused restaurant or restaurant/bar with a brewery on-premise.',
             'large': 'A very large brewery. Likely not for visitors. Ex. Miller-Coors. (deprecated)',
             'planning': 'A brewery in planning or not yet opened to the public.',
             'bar': 'A bar. No brewery equipment on premise. (deprecated)',
             'contract': 'A brewery that uses another brewery’s equipment.',
             'proprietor': 'Similar to contract brewing but refers more to a brewery incubator. closed'
             }
    return list(types.keys())


