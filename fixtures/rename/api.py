from fixtures.constants import Links
from fixtures.request import Request
def rename_file(url_check):
    response = Request("Rename file").send_request(method="PATCH",
                                                   url=f'{url_check}{Links.DOWNLOAD_FILE_ID}',
                                                   json={'name': Links.NEW_FILE_NAME},
                                                   headers={"Authorization": f"Bearer {Links.ACCESS_TOKEN}",
                                                            'Content-Type': 'application/json'})
    return response
