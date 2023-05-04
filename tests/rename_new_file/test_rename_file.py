import pytest
from fixtures.rename.api import rename_file
import allure
from fixtures.response import Response
import pytest
from fixtures.constants import Links
@allure.feature("Проверка переименования файла")
@allure.story("Проверка функции переименования файла")
@pytest.mark.positive
def test_rename_file(update_refresh_token):
    with allure.step("Переименование файла на Google Drive"):
        value = rename_file(Links.URL_CHECK)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 200, "Check your link")
    with allure.step("Проверим имя файла"):
        Response.log_assert(value.json().get('name') == "testikk.txt", "Check your link")

@allure.feature("Проверка переименования файла")
@allure.story("Проверка функции переименования файла по неверной ссылке")
@pytest.mark.negative
def test_rename_unknown_file(update_refresh_token):
    with allure.step("Переименование файла на Google Drive"):
        value = rename_file(Links.URL_DOWNLOAD)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 400, "Check your link")
