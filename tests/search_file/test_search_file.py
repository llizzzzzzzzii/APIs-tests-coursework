from fixtures.search.api import search_files
from fixtures.constants import Links
import allure
import pytest
from fixtures.response import Response
from com.jsonschema.search import ResponseSearchFile
from com.jsonschema.error import ResponseError404

@allure.feature("Проверка поиска файла")
@allure.story("Проверка поиска файла 'input.txt'")
@pytest.mark.positive

def test_search_file(update_refresh_token):
    with allure.step("Поиск файла на Google Drive"):
        value = search_files(Links.FILE_NAME, Links.PARENTS)
    with allure.step("Запрос отправлен, проверим тело ответа"):
        Response.validate(value, ResponseSearchFile.schema)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 200, "Check file name")
    with allure.step("Проверим имя найденного файла"):
        Response.log_assert(value.json()['files'][0]['name'] == Links.FILE_NAME, "Check file name")

@allure.feature("Проверка поиска файла")
@allure.story("Проверка поиска файла с неверными параметрами 'input.txt'")
@pytest.mark.negative
def test_search_unknown_file(update_refresh_token):
    with allure.step("Поиск файла с неверным ID в неверной папке на Google Drive"):
        value = search_files(Links.FILE_NAME_INCORR, Links.PARENTS_INCORR)
    with allure.step("Запрос отправлен, проверим тело ответа"):
        Response.validate(value, ResponseError404.schema)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 404, "Check file name")
