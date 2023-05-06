import logging
import jsonschema
from fixtures.deco import LogResponse

class Response:
    @staticmethod
    def log_assert(func, message):
        if not func:
            logging.error(message)
        assert func, message

    @staticmethod
    def validate(response, schema):
        try:
            jsonschema.validate(instance=response.json(), schema=schema)
            LogResponse.logger.info("Correct json")
        except BaseException:
            LogResponse.logger.warning("Wrong json")
