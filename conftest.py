import pytest
from fixtures.constants import Links
from fixtures.request import request
from fixtures.deco import logging as log

@log("Update refresh token")
def update_refresh_token_api():
    token_data = {
        'refresh_token': Links.REFRESH_TOKEN,
        'client_id': Links.CLIENT_ID,
        'client_secret': Links.CLIENT_SECRET,
        'grant_type': 'refresh_token',
    }
    response = request(method="POST",
                       url=Links.TOKEN_URL,
                       data=token_data,
                       )
    return response

@pytest.fixture()
def update_refresh_token():
    response = update_refresh_token_api()
    if response.ok:
        token = response.json()['access_token']
        return token
    else:
        return None