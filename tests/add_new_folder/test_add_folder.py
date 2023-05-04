import pytest
from fixtures.add_folder.api import add_new_folder
from fixtures.constants import Links
import allure
from fixtures.response import Response

@allure.feature("Проверка создания папки")
@allure.story("Проверка функции создания папки")
@pytest.mark.positive
def test_add_folder(update_refresh_token):
    with allure.step("Создание папки на Google Drive"):
        value = add_new_folder(Links.PARENTS)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 200, "Check your parents ID")
    with allure.step("Проверим имя папки"):
        Response.log_assert(value.json().get('name') == "test_folder", "Check your parents ID")

@allure.feature("Проверка создания файла")
@allure.story("Проверка функции создания папки по неверной ссылке ")
@pytest.mark.negative
def test_add_unknown_folder(update_refresh_token):
    with allure.step("Создание папки по неверной ссылке на Google Drive"):
        value = add_new_folder('')
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 404, "Check parents ID")

