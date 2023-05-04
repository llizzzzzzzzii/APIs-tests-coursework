from fixtures.constants import Links
import requests
from fixtures.request import Request
def edit_file():
    url = f"{Links.URL_UPLOAD}{Links.EDIT_FILE_ID}"
    headers = {"Authorization": f"Bearer {Links.ACCESS_TOKEN}", "Content-Type": "text/plain"}
    data = "test file"
    response = requests.patch(url, headers=headers, data=data)
    return response