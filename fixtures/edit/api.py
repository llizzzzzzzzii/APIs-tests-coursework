from fixtures.constants import Links
from fixtures.request import Request

# функция для редактирования содержимого файла
def edit_file(file_id):
    response = Request("Edit file").send_request(method="PATCH",
                                                   url=f'{Links.URL_UPLOAD}{file_id}',
                                                   data="testik file",
                                                   headers={"Authorization": f"Bearer {Links.ACCESS_TOKEN}",
                                                            'Content-Type': "text/plain"})
    return response
