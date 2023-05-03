import pytest
from fixtures.rename.api import rename_file
import allure

@allure.feature("Проверка переименования папки")
@allure.story("Проверка функции переименования файла")
@pytest.mark.positive
def test_add_label(update_refresh_token):
    with allure.step("Переименование файла на Google Drive"):
        value=rename_file()
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert value.status_code==200, "Check your file ID"
    with allure.step("Проверим имя файла"):
        assert value.json().get('name') == "testik.txt", "Check your file ID"