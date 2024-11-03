import os
import pytest
import requests

@pytest.fixture
def function_url():
    """
    Retrieves the Cloud Function URL from an environment variable.
    """
    url = os.environ.get('FUNCTION_URL')
    assert url is not None, "FUNCTION_URL environment variable is not set"
    return url

def test_function_basic(function_url):
    """
    Test the function with no query parameters.
    """
    response = requests.get(function_url)
    assert response.status_code == 200
    assert response.text == 'Hello, World!'

def test_function_with_name(function_url):
    """
    Test the function with a 'name' query parameter.
    """
    response = requests.get(function_url, params={'name': 'Bob'})
    assert response.status_code == 200
    assert response.text == 'Hello, Bob!'

def test_function_with_json_payload(function_url):
    """
    Test the function with a JSON payload.
    """
    response = requests.post(
        function_url,
        json={'name': 'Charlie'}
    )
    assert response.status_code == 200
    assert response.text == 'Hello, Charlie!'
