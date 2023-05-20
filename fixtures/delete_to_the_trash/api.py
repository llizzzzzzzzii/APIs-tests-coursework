from fixtures.constants import Links
from fixtures.request import Request

# функция для удаления файла в корзину
def delete_file_to_the_trash(file_id):
    response = Request("Delete file to the trash").send_request(method="POST",
                                                   url=f'{Links.URL_DELETE}{file_id}/trash',
                                                   headers={'Authorization': f'Bearer {Links.ACCESS_TOKEN}',
                                                            'Content-Type': 'application/json'})
    return response

