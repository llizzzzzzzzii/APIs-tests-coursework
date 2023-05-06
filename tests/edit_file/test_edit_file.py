import pytest
from fixtures.constants import Links
from fixtures.edit.api import edit_file
import allure
from fixtures.response import Response
from com.jsonschema.file import FileResponse
from com.jsonschema.error import ResponseError404

@allure.feature("Проверка изменения содержимого файла")
@allure.story("Проверка функции изменения содержимого файла")
@pytest.mark.positive
def test_edit_file(update_refresh_token):
    with allure.step("Изменение содержимого файла на Google Drive"):
        value = edit_file(Links.EDIT_FILE_ID)
    with allure.step("Запрос отправлен, проверим тело ответа"):
        Response.validate(value, FileResponse.schema)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 200, "Check your file ID")
    with allure.step("Проверим имя файла, который изменяли"):
        Response.log_assert(value.json().get('name') == "test_edit_file.txt", "Check your file ID")

@allure.feature("Проверка изменения содержимого файла")
@allure.story("Проверка функции изменения содержимого файла с неверным ID")
@pytest.mark.negative
def test_edit_unknown_file(update_refresh_token):
    with allure.step("Изменение содержимого файла с неверным ID на Google Drive"):
        value = edit_file(Links.FILE_ID)
    with allure.step("Запрос отправлен, проверим тело ответа"):
        Response.validate(value, ResponseError404.schema)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 404, "Check your file ID")
