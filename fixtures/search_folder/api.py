from fixtures.request import Request
from fixtures.constants import Links

def search_folder():
    response = Request("Search Files").send_request(method="GET",
                       url="https://www.googleapis.com/drive/v3/files",
                       params={"q": "name='python' and mimeType='application/vnd.google-apps.folder'",
                               "fields": "files(id)",
                               "access_token": f"{Links.ACCESS_TOKEN}"})
    return response
