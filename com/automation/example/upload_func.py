import json
import os

import pytest
import requests
from constants import Links
from com.automation.example.refresh_new_token import *
def upload_file(file_name):
    access_token = refresh_token(Links.REFRESH_TOKEN)
    # file_name = Links.FILE_NAME
    file_path = os.path.join(os.getcwd(), file_name)
    url = Links.URL_DOWNLOAD
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"name": file_name, "parents": ["1Geg7D6y-7wueDGxoGFFtDfvjrVUDTVwr"]}
    files = {"data": ("metadata", json.dumps(params), "application/json; charset=UTF-8"),
             "file": open(file_path, "rb")}
    response = requests.post(url, headers=headers, files=files)
    file_id = response.json()["id"]
    print(file_id)
    url1 = f"https://www.googleapis.com/drive/v3/files/{file_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url1, headers=headers)
    return response
