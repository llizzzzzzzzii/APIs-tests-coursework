import logging

class Response:
    @staticmethod
    def log_assert(func, message):
        if not func:
            logging.error(message)
        assert func, message