import requests
from requests import Response
from fixtures.deco import logger

class Request:
    def __init__(self, name) -> None:
        self.name = name
        pass

    def send_request(self, method: str, url: str, **kwargs) -> Response:
        try:
            response = requests.request(method, url, **kwargs)
            logger.info(self.name)
            log_response = f"Response method: {method}, url: {url}, status: {response.status_code}"
            logger.info(log_response)
            return response
        except requests.exceptions.ConnectionError as e:
            logger.exception(f"ConnectionError: {e}")
