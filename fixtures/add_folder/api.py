import requests
from fixtures.constants import Links
from fixtures.request import Request

def add_new_folder():
    response = Request("Add new folder").send_request(method="POST",
                                                      url='https://www.googleapis.com/drive/v3/files',
                                                      headers={'Authorization': f'Bearer {Links.ACCESS_TOKEN}',\
                                                               'Content-Type': 'application/json'},
                                                      json={'name': Links.FOLDER_NAME,
                                                            'parents': [Links.PARENTS],
                                                            'mimeType': 'application/vnd.google-apps.folder'})
    return response
