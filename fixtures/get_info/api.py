from fixtures.constants import Links
from fixtures.request import Request

# функция для получения даты и времени создания файла
def get_info(file_id):
    response = Request("Get_info_about_file").send_request(method="GET",
                                                   url=f'{Links.URL_CHECK}{file_id}',
                                                   params="fields=createdTime,size",
                                                   headers={"Authorization": f"Bearer {Links.ACCESS_TOKEN}"})
    return response
