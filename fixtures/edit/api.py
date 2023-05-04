from fixtures.constants import Links
import requests
from fixtures.request import Request
def edit_file(file_id):
    url = f"{Links.URL_UPLOAD}{file_id}"
    headers = {"Authorization": f"Bearer {Links.ACCESS_TOKEN}", "Content-Type": "text/plain"}
    data = "testt file"
    response = requests.patch(url, headers=headers, data=data)
    return response