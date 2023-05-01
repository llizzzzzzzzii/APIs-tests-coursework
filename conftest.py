import pytest
from fixtures.constants import Links
import requests
from fixtures.deco import logging as log

@log("Update refresh token")
def update_refresh_token_api():
    token_url = Links.TOKEN_URL
    token_data = {
        'refresh_token': Links.REFRESH_TOKEN,
        'client_id': Links.CLIENT_ID,
        'client_secret': Links.CLIENT_SECRET,
        'grant_type': 'refresh_token',
    }
    return requests.post(token_url, data=token_data)

@pytest.fixture()
def update_refresh_token():
    response = update_refresh_token_api()
    if response.ok:
        token = response.json()['access_token']
        return token
    else:
        return None