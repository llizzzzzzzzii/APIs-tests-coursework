from fixtures.constants import Links
from fixtures.request import Request

# функция для возврата файла из корзины
def restore_file(file_id):
    response = Request("Restore file from the trash").send_request(method="POST",
                                                   url=f'{Links.URL_DELETE}{file_id}/untrash',
                                                   headers={'Authorization': f'Bearer {Links.ACCESS_TOKEN}',
                                                            'Content-Type': 'application/json'})
    return response
