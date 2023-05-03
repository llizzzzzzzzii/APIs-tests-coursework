import requests
from fixtures.constants import Links
def search_folder():
    url = "https://www.googleapis.com/drive/v3/files"
    params = {
        "q": "name='python' and mimeType='application/vnd.google-apps.folder'",
        "fields": "files(id)",
        "access_token": f"{Links.ACCESS_TOKEN}"
    }
    response = requests.get(url, params=params)
    return response
