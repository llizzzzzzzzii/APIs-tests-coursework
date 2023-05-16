import pytest
from fixtures.constants import Links
from fixtures.request import Request
import json
import os
import requests

def update_refresh_token_api():
    token_data = {
        'refresh_token': Links.REFRESH_TOKEN,
        'client_id': Links.CLIENT_ID,
        'client_secret': Links.CLIENT_SECRET,
        'grant_type': 'refresh_token',
    }
    response = Request("Update refresh token").send_request(method="POST",
                       url=Links.TOKEN_URL,
                       data=token_data)
    return response

@pytest.fixture()
def update_refresh_token():
    response = update_refresh_token_api()
    if response.ok:
        token = response.json()['access_token']
        Links.ACCESS_TOKEN = token
        return token
    else:
        return None

@pytest.fixture()
def get_file_id():
    file_path = os.path.join(os.getcwd(), Links.FILE_PATH)
    headers = {"Authorization": f"Bearer {Links.ACCESS_TOKEN}"}
    params = {"name": Links.FILE_NAME, "parents": [Links.PARENTS]}
    files = {"data": ("metadata", json.dumps(params),
                      "application/json; charset=UTF-8"),
             "file": open(file_path, "rb")}
    response = requests.post(Links.URL_DOWNLOAD, headers=headers, files=files)
    Links.FILE_ID_CORR = response.json()["id"]
    return response.json()["id"]
