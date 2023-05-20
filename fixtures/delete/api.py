from fixtures.request import Request
from fixtures.constants import Links

# функция для удаления файла
def delete_file(file_id):
    response = Request("Delete file").send_request(method="DELETE",
                       url=f"{Links.URL_CHECK}{file_id}",
                       headers={"Authorization": f"Bearer {Links.ACCESS_TOKEN}"})
    return response

