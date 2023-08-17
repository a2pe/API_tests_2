import random
import pytest
import requests
from conftest import get_breweries, get_brewery_cities, get_several_brewery_ids, brewery_types
from python_tests_2.test_api_service.files_with_expected_responses.data import data


@pytest.mark.smoke
def test_list_all_breweries(base_url):
    """Testing the API endpoint for returning the list of all breweries."""
    response = requests.get(base_url).json()
    assert response == data


@pytest.mark.smoke
def test_list_one_brewery(base_url, single_brewery):
    """Testing the API endpoint for returning a brewery."""
    response = requests.get(base_url + "/" + single_brewery).json()
    assert response['id'] == single_brewery


# @pytest.mark.smoke
# def test_list_single_brewery_2(base_url, single_brewery):
#     response = requests.get(base_url + "/" + single_brewery)
#     assert response.status_code == 200


@pytest.mark.parametrize('param', get_breweries())
def test_list_each_brewery(base_url, param):
    """Testing the API endpoint for returning each brewery."""
    response = requests.get(base_url + "/" + param)
    assert response.status_code == 200


@pytest.mark.parametrize('city', get_brewery_cities())
def test_list_all_breweries_by_city(base_url, city):
    """Testing the API endpoint for returning available breweries by city."""
    params = {'by_city': city, 'per_page': random.randint(0, 100)}
    response = requests.get(base_url, params=params)
    assert response.status_code == 200
    for data in response.json():
        assert city in data.get('city')


@pytest.mark.smoke
def test_list_breweries_by_ids(base_url):
    """Testing the API endpoint for returning breweries by the specified ids."""
    brewery_ids = get_several_brewery_ids()
    params = {'by_ids': ','.join(brewery_ids)}
    response = requests.get(base_url, params=params)
    assert response.status_code == 200
    assert len(response.json()) == len(brewery_ids)
    assert {data.get('id') for data in response.json()} == set(brewery_ids)


@pytest.mark.parametrize('param', brewery_types())
def test_list_brewery_of_specific_type(base_url, param):
    """Testing the API endpoint for returning breweries by the specific type."""
    params = {'by_type': param}
    response = requests.get(base_url, params=params).json()
    response_type = response[1]['brewery_type']
    assert response_type == param
