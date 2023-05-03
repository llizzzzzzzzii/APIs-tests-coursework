import requests
from fixtures.constants import Links
def search_files(update_refresh_token,file_name,parents):
    access_token=update_refresh_token
    url = Links.URL_CHECK
    params = {"q": f"name='{file_name}' and '{parents}' in parents"}
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, params=params, headers=headers)
    return response