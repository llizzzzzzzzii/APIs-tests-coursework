from fixtures.request import Request

# функция для поиска папки
def search_folder(access_token):
    response = Request("Search Folder").send_request(method="GET",
                       url="https://www.googleapis.com/drive/v3/files",
                       params={"q": "name='python' and mimeType='application/vnd.google-apps.folder'",
                               "fields": "files(id)",
                               "access_token": f"{access_token}"})
    return response
