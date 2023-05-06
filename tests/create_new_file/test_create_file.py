import pytest
from fixtures.create.api import create_file
import allure
from fixtures.response import Response
from fixtures.constants import Links
from com.jsonschema.file import FileResponse
from com.jsonschema.error import ResponseError404

@allure.feature("Проверка создания пустого файла")
@allure.story("Проверка функции создания нового файла")
@pytest.mark.positive
def test_create_file(update_refresh_token):
    with allure.step("Загрузка нового файла на Google Drive"):
        value = create_file(Links.PARENTS)
    with allure.step("Запрос отправлен, проверим тело ответа"):
        Response.validate(value, FileResponse.schema)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 200, "Check your parents ID")
    with allure.step("Проверим имя файла, который загружали"):
        Response.log_assert(value.json().get('name') == Links.CREATE_FILE_NAME, "Check your folder ID")

@allure.feature("Проверка создания пустого файла")
@allure.story("Проверка функции создания нового файла в папке с неверным ID")
@pytest.mark.negative
def test_create_unknown_file(update_refresh_token):
    with allure.step("Загрузка нового файла на Google Drive"):
        value = create_file(Links.PARENTS_INCORR)
    with allure.step("Запрос отправлен, проверим тело ответа"):
        Response.validate(value, ResponseError404.schema)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 404, "Check your parents ID")
