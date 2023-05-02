from fixtures.constants import Links
from fixtures.deco import logging as log
from fixtures.request import request

@log("Download file")
def download_file(file_id):
    response = request(method="GET",
                       url=f'{Links.URL_CHECK}{file_id}?alt=media',
                       headers={"Authorization": f"Bearer {Links.ACCESS_TOKEN}"})
    with open(Links.DOWNLOAD_FILE_NAME, 'wb') as f:
        f.write(response.content)
    return response