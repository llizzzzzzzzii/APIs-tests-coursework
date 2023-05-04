import pytest
from fixtures.search_folder.api import search_folder
from fixtures.constants import Links
import allure
from fixtures.response import Response

@allure.feature("Проверка поиска папки")
@allure.story("Проверка функции поиска папки 'python'")
@pytest.mark.positive
def test_search_folder(update_refresh_token):
    with allure.step("Поиск папки на Google Drive"):
        value = search_folder(Links.ACCESS_TOKEN)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 200, "Check your access token")
    with allure.step("Проверим ID найденной папки"):
        Response.log_assert(value.json()['files'][0]['id'] == Links.PARENTS, "Check your access token")

@allure.feature("Проверка поиска папки")
@allure.story("Проверка функции поиска папки 'python'")
@pytest.mark.positive
def test_search_folder_without_token(update_refresh_token):
    with allure.step("Поиск папки на Google Drive без токена"):
        value = search_folder('')
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 403, "Check your access token")
