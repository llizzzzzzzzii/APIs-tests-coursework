import requests
from fixtures.constants import Links
def rename_file():
    headers = {
            'Authorization': f'Bearer {Links.ACCESS_TOKEN}',
            'Content-Type': 'application/json'
        }
    url = f'{Links.URL_CHECK}{Links.DOWNLOAD_FILE_ID}'

    data = {
            'name': Links.NEW_FILE_NAME
        }
    response = requests.patch(url, headers=headers, json=data)
    return response
