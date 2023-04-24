from fixtures.constants import Links
import requests

def get_token():
    auth_url = ('https://accounts.google.com/o/oauth2/auth?'
                'client_id={}&redirect_uri={}&scope=https://www.googleapis.com/auth/drive&response_type=code&access_type=offline'
                .format(Links.CLIENT_ID, Links.REDIRECT_URI, Links.SCOPE))
    print('Откройте ссылку в браузере:\n{}'.format(auth_url))
    authorization_code = input('Введите код авторизации: ')
    token_url = Links.TOKEN_URL
    token_data = {
        'code': authorization_code,
        'client_id': Links.CLIENT_ID,
        'client_secret': Links.CLIENT_SECRET,
        'redirect_uri': Links.REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    response = requests.post(token_url, data=token_data)
    print(response)
    if response.ok:
        token = response.json()['access_token']
        refresh_token = response.json()['refresh_token']
        print('Токен получен успешно.')
        print('access_token = {}'.format(token))
        print('refresh_token = {}'.format(refresh_token))
        return token, refresh_token
    else:
        print('Ошибка при получении токена:')
        print(response.content)
        return None, None