from com.get_token.api import get_token_api

def get_token():
    response = get_token_api()
    if response.ok:
        token = response.json()['access_token']
        refresh_token = response.json()['refresh_token']
        return token, refresh_token
    else:
        return None, None