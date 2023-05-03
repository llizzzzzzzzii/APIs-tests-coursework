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
        value = search_folder()
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 200, "Check your folder ID")
    with allure.step("Проверим ID найденной папки"):
        Response.log_assert(value.json()['files'][0]['id'] == Links.PARENTS, "Check you folder ID")
