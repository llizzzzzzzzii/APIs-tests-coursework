from fixtures.deco import logging as log
from fixtures.constants import Links
from fixtures.request import Request
from com.get_token.get_token import get_token_json

def get_token_api():
    response = Request("Get Tokens").send_request(method="POST",
                       url=Links.TOKEN_URL,
                       json=get_token_json()
                       )
    return response
