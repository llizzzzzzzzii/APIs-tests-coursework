import requests
from fixtures.constants import Links
def add_new_folder():
    headers = {
        'Authorization': f'Bearer {Links.ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'name': Links.FOLDER_NAME,
        'parents': [Links.PARENTS],
        'mimeType': 'application/vnd.google-apps.folder'
    }
    response = requests.post(Links.URL_ADD, headers=headers, json=data)
    return response
