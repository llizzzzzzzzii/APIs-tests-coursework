from fixtures.search.api import search_files
from fixtures.constants import Links
import allure
import pytest

@allure.feature("Проверка поиска файла")
@allure.story("Проверка поиска файла 'input.txt'")
@pytest.mark.positive

def test_search_file(update_refresh_token):
    with allure.step("Поиск файла на Google Drive"):
        value=search_files(update_refresh_token,Links.FILE_NAME,Links.PARENTS)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert value.status_code==200
    with allure.step("Проверим имя найденного файла"):
        assert value.json()['files'][0]['name']==Links.FILE_NAME

def test_search_unknown_file(update_refresh_token):
    with allure.step("Поиск файла с неверным ID в неверной папке на Google Drive"):
        value=search_files(update_refresh_token,Links.FILE_NAME_INCORR,Links.PARENTS_INCORR)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert value.status_code==404
