from fixtures.constants import Links
from fixtures.request import Request

def add_new_folder(parents):
    response = Request("Add new folder").send_request(method="POST",
                                                      url=f"{Links.URL_CHECK}",
                                                      headers={'Authorization': f'Bearer {Links.ACCESS_TOKEN}',\
                                                               'Content-Type': 'application/json'},
                                                      json={'name': Links.FOLDER_NAME,
                                                            'parents': [parents],
                                                            'mimeType': 'application/vnd.google-apps.folder'})
    return response
