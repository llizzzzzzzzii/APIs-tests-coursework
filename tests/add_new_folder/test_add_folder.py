import pytest
from fixtures.add_folder.api import add_new_folder
import allure
from fixtures.response import Response

@allure.feature("Проверка создания папки")
@allure.story("Проверка функции создания папки")
@pytest.mark.positive
def test_add_folder(update_refresh_token):
    with allure.step("Создание папки на Google Drive"):
        value = add_new_folder()
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 200, "Check your folder ID")
    with allure.step("Проверим имя папки"):
        Response.log_assert(value.json().get('name') == "test_folder", "Check your folder ID")

