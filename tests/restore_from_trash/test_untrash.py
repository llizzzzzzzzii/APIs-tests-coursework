import pytest
from fixtures.delete_to_the_trash.api import delete_file_to_the_trash
from fixtures.untrash.api import untrash
from fixtures.upload.api import upload_file
from fixtures.constants import Links
import allure
from fixtures.response import Response

@allure.feature("Проверка восстановление файла из корзины")
@allure.story("Проверка функции восстановления файла 'input.txt' из корзины")
@pytest.mark.positive
def test_delete_file_to_trash(update_refresh_token, get_file_id):
    with allure.step("Восстановление файла из корзины Google Drive"):
        delete_file_to_the_trash(upload_file(Links.URL_CHECK).json()['id'])
        value = untrash(Links.FILE_ID_CORR)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 200, "Check your file ID")
    with allure.step("Проверим имя файла, который был восстановлен"):
        Response.log_assert(value.json().get('originalFilename') == Links.FILE_NAME, 'Check your file ID')

@allure.feature("Проверка восстановление файла из корзины")
@allure.story("Проверка функции восстановления файла 'input.txt' из корзины")
@pytest.mark.negative
def test_delete_unknown_file_to_trash(update_refresh_token):
    with allure.step("Восстановление файла из корзины Google Drive"):
        value = untrash(delete_file_to_the_trash(Links.FILE_ID))
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 404, "Check your file ID")
