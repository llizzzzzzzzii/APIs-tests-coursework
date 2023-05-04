import pytest
from fixtures.rename.api import rename_file
import allure
from fixtures.response import Response

@allure.feature("Проверка переименования папки")
@allure.story("Проверка функции переименования файла")
@pytest.mark.positive
def test_rename_file(update_refresh_token):
    with allure.step("Переименование файла на Google Drive"):
        value = rename_file()
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 200, "Check your file ID")
    with allure.step("Проверим имя файла"):
        Response.log_assert(value.json().get('name') == "testik.txt", "Check your file ID")