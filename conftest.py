import pytest
from fixtures.constants import Links
import requests

@pytest.fixture()
def update_refresh_token():
    token_url = Links.TOKEN_URL
    token_data = {
        'refresh_token': Links.REFRESH_TOKEN,
        'client_id': Links.CLIENT_ID,
        'client_secret': Links.CLIENT_SECRET,
        'grant_type': 'refresh_token',
    }
    response = requests.post(token_url, data=token_data)
    if response.ok:
        token = response.json()['access_token']
        print('Токен обновлен успешно.')
        print('access_token = {}'.format(token))
        return token
    else:
        print('Ошибка при обновлении токена:')
        print(response.content)
        return None