import json
import os
import pytest
import requests
from fixtures.constants import *
def upload_file(update_refresh_token):
    access_token = update_refresh_token
    file_path = os.path.join(os.getcwd(), Links.FILE_NAME)
    url = Links.URL_DOWNLOAD
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"name": Links.FILE_NAME, "parents": [Links.PARENTS]}
    files = {"data": ("metadata", json.dumps(params), "application/json; charset=UTF-8"),
             "file": open(file_path, "rb")}
    response = requests.post(url, headers=headers, files=files)
    file_id = response.json()["id"]
    print(file_id)
    url1 = f"https://www.googleapis.com/drive/v3/files/{file_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url1, headers=headers)
    return response
