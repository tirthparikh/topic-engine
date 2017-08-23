from unittest import mock

import requests

from topic_engine.crawler import Crawler


def test_check_connection_for_Invalid_Url():
    c = Crawler("zenpencils.com")
    assert c.check_connection() == (
        False,
        "Invalid URL zenpencils.com, Please remember to add http:// or the domain name ")


@mock.patch("requests.get")
class TestClassforcheckconnection:
    URL = "http://google.com"
    c = Crawler(URL)
    def test_check_connection_for_HTTPError(self, mock_get):
        """Testing the check_connection method for HTTPError"""
        mock_response = mock.Mock()
        http_error = requests.exceptions.HTTPError()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = http_error

        # Assign our mock response as the result of our patched function
        mock_get.return_value = mock_response
        assert self.c.check_connection() == (
            False,
            "HTTPError :404")

    def test_check_connection_for_Timeout(self, mock_get):
        """Testing the check_connection method for Timeouterror"""
        mock_response = mock.Mock()
        timeout_error = requests.exceptions.Timeout()

        mock_response.raise_for_status.side_effect = timeout_error
        mock_get.return_value = mock_response
        assert self.c.check_connection() == (
            False,
            "Connection Timeout! Please retry.")

    def test_check_connection_for_TooManyRedirects(self, mock_get):
        """Testing the check_connection method for Too Many Redirects"""
        mock_response = mock.Mock()
        timeout_error = requests.exceptions.TooManyRedirects()

        mock_response.raise_for_status.side_effect = timeout_error
        mock_get.return_value = mock_response
        assert self.c.check_connection() == (
            False,
            "Too Many Redirects! Please refresh check the URL")

    def test_check_connection_for_Connection_Error(self, mock_get):
        """Testing the check_connection method for Timeouterror"""
        mock_response = mock.Mock()
        timeout_error = requests.exceptions.ConnectionError()

        mock_response.raise_for_status.side_effect = timeout_error
        mock_get.return_value = mock_response
        assert self.c.check_connection() == (
            False, "Connection Error! PLease check you Connections")