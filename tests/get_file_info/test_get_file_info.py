import pytest
from fixtures.get_info.api import get_info
import allure
from fixtures.response import Response
import pytest
from fixtures.constants import Links

@allure.feature("Проверка получения информации о файле")
@allure.story("Проверка функции получения даты создания и размера файла")
@pytest.mark.positive
def test_get_file_info(update_refresh_token):
    with allure.step("Получение информации о файле на Google Drive"):
        value = get_info(Links.ID_FILE)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 200, "Check your file ID")
    with allure.step("Проверим размер файла"):
        Response.log_assert(value.json()['size'] == '10', "Check your file ID")
    with allure.step("Проверим год создания файла"):
        Response.log_assert(value.json()["createdTime"] == Links.DATE, "Check your file ID")

@allure.feature("Проверка получения информации о файле")
@allure.story("Проверка функции получения даты создания и размера файла с неизвестным ID")
@pytest.mark.negative
def test_get_unknown_file_info(update_refresh_token):
    with allure.step("Получение информации о файле на Google Drive"):
        value = get_info(Links.FILE_ID)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 404, "Check your file ID")
