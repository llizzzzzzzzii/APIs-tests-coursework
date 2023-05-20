from fixtures.constants import Links
from fixtures.request import Request

# функция для скачивания файла
def download_file(file_id):
    response = Request("Download file").send_request(method="GET",
                       url=f'{Links.URL_CHECK}{file_id}?alt=media',
                       headers={"Authorization": f"Bearer {Links.ACCESS_TOKEN}"})
    
    with open(f'{Links.FOLDER_PATH}/{Links.DOWNLOAD_FILE_NAME}','wb') as f:
        f.write(response.content)
    return response