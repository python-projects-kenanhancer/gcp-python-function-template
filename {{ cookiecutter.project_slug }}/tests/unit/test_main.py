import pytest
from flask import Request
from werkzeug.test import EnvironBuilder
from werkzeug.wrappers import Request as WerkzeugRequest

# Import your function from the function directory
from function.main import main


@pytest.fixture
def mock_request():
    """
    Create a mock Flask request object with query parameter 'name=Tester'.
    """
    builder = EnvironBuilder(method="GET", query_string={"name": "Tester"})
    env = builder.get_environ()
    request = Request(WerkzeugRequest(env))
    return request


class TestMainFunction:

    def test_main(self, mock_request):
        """
        Test the main function with a mock request containing 'name=Tester'.
        """
        response = main(mock_request)
        assert response.status_code == 200
        assert response.get_data(as_text=True) == "Hello, Tester!"
        assert response.mimetype == "text/plain"

    def test_main_no_name(self):
        """
        Test the main function with no name provided in query parameters.
        """
        builder = EnvironBuilder(method="GET")
        env = builder.get_environ()
        request = Request(WerkzeugRequest(env))
        response = main(request)
        assert response.status_code == 200
        assert response.get_data(as_text=True) == "Hello, World!"

    def test_main_json_payload(self):
        """
        Test the main function with a JSON payload containing 'name': 'Alice'.
        """
        builder = EnvironBuilder(
            method="POST", content_type="application/json", data='{"name": "Alice"}'
        )
        env = builder.get_environ()
        request = Request(WerkzeugRequest(env))
        response = main(request)
        assert response.status_code == 200
        assert response.get_data(as_text=True) == "Hello, Alice!"
