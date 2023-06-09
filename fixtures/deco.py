import json
import logging
import pprint
from functools import wraps
from json import JSONDecodeError

#логирование для обработки ответов
class LogResponse:
    logger = logging.getLogger("response")
    logger.setLevel(logging.INFO)
    s_handler = logging.StreamHandler()
    s_format = logging.Formatter('%(name)s %(levelname)s - %(message)s')
    s_handler.setFormatter(s_format)
    logger.addHandler(s_handler)

#логирование для запросов
class LogRequest:
    logger = logging.getLogger("api")
    logger.setLevel(logging.INFO)
    s_handler = logging.StreamHandler()
    s_format = logging.Formatter('%(name)s %(levelname)s - %(message)s')
    s_handler.setFormatter(s_format)
    logger.addHandler(s_handler)

    def logging(message):
        """
        Request Logging
        :return: response
        """
        def wrapper(function):
            @wraps(function)
            def inner(*args, **kwargs):
                LogRequest.logger.info(message)
                res = function(*args, **kwargs)
                method = res.request.method
                url = res.request.url
                body = res.request.body
                status = res.status_code
                body_sep = " "
                log_request = f"Request method: {method}, url: {url}"
                if body is not None:
                    try:
                        json_body = json.dumps(
                            json.loads(body.decode("utf-8")), indent=4, ensure_ascii=False
                        )
                        if len(body) > 20:
                            body_sep = "\n"
                        log_request += (
                            f", body:{body_sep}{json_body or pprint.pformat(body)}"
                        )
                    except AttributeError:
                        log_request += f", body:{body}"
                LogRequest.logger.info(log_request)

                log_response = f"Response method: {method}, url: {url}, status: {status}"
                try:
                    body = res.json()
                    if len(res.content) > 20:
                        body_sep = "\n"
                        bd = json.dumps(body, indent=4, ensure_ascii=False)
                        log_response += f", body:{body_sep}{bd}"
                    else:
                        log_response += f", body:{json.dumps(body)}"
                    LogRequest.logger.info(log_response)
                except JSONDecodeError:
                    if len(res.text) > 120:
                        log_response += f", body: {res.text[:120]}..."
                    else:
                        log_response += f", body: {res.text}"
                    LogRequest.logger.info(log_response)
                return res

            return inner

        return wrapper