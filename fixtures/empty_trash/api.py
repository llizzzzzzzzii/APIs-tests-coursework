from fixtures.constants import Links
from fixtures.request import Request

# функция для очистки корзины
def empty_trash(url_delete):
    response = Request("Empty trash").send_request(method="DELETE",
                                                   url=f'{url_delete}trash',
                                                   json='',
                                                   headers={'Authorization': f'Bearer {Links.ACCESS_TOKEN}',
                                                            'Content-Type': 'application/json'})
    return response
