import pytest
from fixtures.delete_to_the_trash.api import delete_file_to_the_trash
from fixtures.upload.api import upload_file
from fixtures.constants import Links
import allure
from fixtures.response import Response

@allure.feature("Проверка удаления файла в корзину")
@allure.story("Проверка функции удаления файла 'input.txt' в корзину")
@pytest.mark.positive
def test_delete_file_to_trash(update_refresh_token,get_file_id):
    with allure.step("Удаление файла в корзину с Google Drive"):
        value=delete_file_to_the_trash(upload_file(Links.URL_CHECK).json()['id'])
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 200, "Check your file ID")
    with allure.step("Проверим имя файла, который был удалён"):
        Response.log_assert(value.json().get('originalFilename')==Links.FILE_NAME, 'Check your file ID')

@allure.feature("Проверка удаления файла в корзину")
@allure.story("Проверка функции удаления файла с неизвестным ID в корзину")
@pytest.mark.negative
def test_delete_unknown_file_to_trash(update_refresh_token,get_file_id):
    with allure.step("Удаление файла в корзину с Google Drive"):
        value=delete_file_to_the_trash(Links.FILE_ID)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 404, "Check your file ID")