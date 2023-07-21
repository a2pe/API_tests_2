import requests


def test_url_response(url, status_code):
    response = requests.get(url).status_code
    assert str(response) == str(status_code)
