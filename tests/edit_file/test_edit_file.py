import pytest
from fixtures.edit.api import edit_file
import allure
from fixtures.response import Response

@allure.feature("Проверка изменения содержимого файла")
@allure.story("Проверка функции изменения содержимого файла")
@pytest.mark.positive
def test_edit_file(update_refresh_token):
    with allure.step("Изменение содержимого файла на Google Drive"):
        value = edit_file()
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 200, "Check your file ID")
    with allure.step("Проверим имя файла, который изменяли"):
        Response.log_assert(value.json().get('name') == "test_edit_file.txt", "Check your folder ID")

