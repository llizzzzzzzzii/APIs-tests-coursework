from fixtures.constants import Links
import requests
from fixtures.request import Request
def get_info(file_id):
    url = f"{Links.URL_CHECK}{file_id}"
    headers = {"Authorization": f"Bearer {Links.ACCESS_TOKEN}"}
    params = "fields=createdTime,size"
    response = requests.get(url, headers=headers, params=params)
    return response