import json
import logging
import os
import pytest
import requests
from fixtures.constants import *
from com.deco import logging as log


# @log("Upload new file")
def upload_file(update_refresh_token,url_down,url_check):
        access_token = update_refresh_token
        file_path = os.path.join(os.getcwd(), Links.FILE_NAME)
        headers = {"Authorization": f"Bearer {access_token}"}
        params = {"name": Links.FILE_NAME, "parents": [Links.PARENTS]}
        files = {"data": ("metadata", json.dumps(params), "application/json; charset=UTF-8"),
                 "file": open(file_path, "rb")}
        response = requests.post(url_down, headers=headers, files=files)
        file_id = response.json()["id"]
        url1 =f"{url_check}{file_id}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url1, headers=headers)
        return response
