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


@pytest.mark.parametrize('param', get_brewery_cities())
def test_list_all_breweries_by_city(base_url, param):
    """Testing the API endpoint for returning available breweries by city."""
    params = {'by_city': param, 'per_page': random.randint(0, 100)}
    response = requests.get(base_url, params=params).json()
    city_from_response = [response[i]['city'] for i in range(1)]
    assert city_from_response == [param]


# Не понимаю, как тут передать ids в params,
# чтобы в итоге запроса был список с этими айдишниками
# (а не список со списками, как сейчас)
# Пришлось огороды городить(
@pytest.mark.smoke
def test_list_breweries_by_ids(base_url):
    """Testing the API endpoint for returning breweries by the specified ids."""
    params = {'by_ids': get_several_brewery_ids()}
    response = [requests.get(base_url, params=params).json() for i in range(len(params['by_ids']))]
    assert len(response) == len(params['by_ids'])


@pytest.mark.parametrize('param', brewery_types())
def test_list_brewery_of_specific_type(base_url, param):
    """Testing the API endpoint for returning breweries by the specific type."""
    params = {'by_type': param}
    response = requests.get(base_url, params=params).json()
    response_type = [response[i]['brewery_type'] for i in range(1)]
    assert response_type == [param]
