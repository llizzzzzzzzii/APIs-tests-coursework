from fixtures.deco import logging as log
from fixtures.constants import Links
from fixtures.request import request
from com.get_token.get_token import *

@log("Get Tokens")
def get_token_api():
    response = request(method="POST",
                       url=Links.TOKEN_URL,
                       json=get_token_json()
                       )
    return response



# from fixtures.deco import logging as log
# from fixtures.constants import Links
# from fixtures.request import request
# import json
#
# @log("Get Tokens")
# def get_token_api():
#     auth_url = (Links.AUTH_URL.format(Links.CLIENT_ID, Links.REDIRECT_URI, Links.SCOPE))
#     print('Откройте ссылку в браузере:\n{}'.format(auth_url))
#     authorization_code = input('Введите код авторизации: ')
#     token_data = {
#         'code': authorization_code,
#         'client_id': Links.CLIENT_ID,
#         'client_secret': Links.CLIENT_SECRET,
#         'redirect_uri': Links.REDIRECT_URI,
#         'grant_type': 'authorization_code'
#     }
#     token_json = json.loads(json.dumps(token_data, default=lambda o: o.__dict__))
#     response = request(method="POST",
#                        url=Links.TOKEN_URL,
#                        json=token_json,
#                        )
#     return response