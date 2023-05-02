import pytest
from fixtures.delete.api import delete_file
from fixtures.upload.api import upload_file
from fixtures.constants import Links
import allure

@allure.feature("Проверка удаления файла")
@allure.story("Проверка функции удаления файла 'input.txt'")
@pytest.mark.positive

def test_delete_file(update_refresh_token):
    with allure.step("Удаление файла с Google Drive"):
        value=delete_file(update_refresh_token,upload_file(update_refresh_token,Links.URL_DOWNLOAD,Links.URL_CHECK).json()["id"])
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert value.status_code==204, "Check your file ID"

@allure.feature("Проверка удаления файла")
@allure.story("Проверка удалился ли файл 'input.txt' с неверным ID")
@pytest.mark.negative

def test_delete_unknown_file(update_refresh_token):
    with allure.step("Удаление файла с неизвестным ID с Google Drive"):
        value=delete_file(update_refresh_token,Links.FILE_ID)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert value.status_code==404, "Check you file ID"




