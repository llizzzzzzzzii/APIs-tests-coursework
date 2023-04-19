import json
import os
import requests
from constants import Links
from com.automation.example.refresh_new_token import *

CLIENT_ID = Links.CLIENT_ID
CLIENT_SECRET = Links.CLIENT_SECRET
REDIRECT_URI = Links.REDIRECT_URI
SCOPE = Links.SCOPE
REFRESH_TOKEN = Links.REFRESH_TOKEN

refresh_token(REFRESH_TOKEN)
def test_upload_file():
    access_token = refresh_token(REFRESH_TOKEN)
    file_name = Links.FILE_NAME
    file_path = os.path.join(os.getcwd(), file_name)
    url = Links.URL_DOWNLOAD
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"name": file_name, "parents": ["1Geg7D6y-7wueDGxoGFFtDfvjrVUDTVwr"]}
    files = {"data": ("metadata", json.dumps(params), "application/json; charset=UTF-8"),
             "file": open(file_path, "rb")}
    response = requests.post(url, headers=headers, files=files)
    assert response.status_code == 200

    file_id = response.json()["id"]
    file_names = response.json()["name"]
    url1 = f"https://www.googleapis.com/drive/v3/files/{file_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url1, headers=headers)

    assert response.status_code == 200
    assert response.json().get('name') == file_names
    assert response.json().get('id') == file_id
