from com.get_token.api import get_token_api
from fixtures.constants import Links
import json

def get_token_json():
    auth_url = (Links.AUTH_URL.format(Links.CLIENT_ID, Links.REDIRECT_URI, Links.SCOPE))
    print('Откройте ссылку в браузере:\n{}'.format(auth_url))
    authorization_code = input('Введите код авторизации: ')
    token_data = {
        'code': authorization_code,
        'client_id': Links.CLIENT_ID,
        'client_secret': Links.CLIENT_SECRET,
        'redirect_uri': Links.REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    return json.loads(json.dumps(token_data, default=lambda o: o.__dict__))

def get_token():
    response = get_token_api()
    if response.ok:
        token = response.json()['access_token']
        refresh_token = response.json()['refresh_token']
        Links.ACCESS_TOKEN = token
        Links.REFRESH_TOKEN = refresh_token
        return token, refresh_token
    else:
        return None, None