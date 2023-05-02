import pytest
from fixtures.upload.api import *
import allure

@allure.feature("Проверка загрузки файла")
@allure.story("Проверка функции загрузки файла 'input.txt'")
@pytest.mark.positive
def test_upload_file(update_refresh_token, get_file_id):
    with allure.step("Загрузка файла на Google Drive"):
        value = upload_file(Links.URL_CHECK)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert value.status_code == 200, 'Check your file ID or file name'
    with allure.step("Проверим имя загруженного файла"):
        assert value.json().get('name') == Links.FILE_NAME, 'Check your file ID or file name'

@allure.feature("Проверка загрузки файла")
@allure.story("Проверка загрузился ли файл 'input.txt' по неверной ссылке")
@pytest.mark.negative
def test_unknown_link(update_refresh_token, get_file_id):
    with allure.step("Загрузка файла на Google Drive"):
        value = upload_file(Links.URL_DOWNLOAD)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert value.status_code == 400, "Check your link"





# import pytest
# from fixtures.upload.api import upload_file
# import allure
# from fixtures.constants import Links
# @allure.feature("Проверка загрузки файла")
# @allure.story("Проверка функции загрузки файла 'input.txt'")
# @pytest.mark.positive
# def test_upload_file(update_refresh_token):
#     with allure.step("Загрузка файла на Google Drive"):
#         value = upload_file(update_refresh_token,
#                             Links.URL_DOWNLOAD, Links.URL_CHECK)
#     with allure.step("Запрос отправлен, посмотрим код ответа"):
#         assert value.status_code == 200, \
#             'Check your file ID or file name'
#     with allure.step("Проверим имя загруженного файла"):
#         assert value.json().get('name') == Links.FILE_NAME, \
#             'Check your file ID or file name'
#
# @allure.feature("Проверка загрузки файла")
# @allure.story("Проверка загрузился ли файл 'input.txt' по неверной ссылке")
# @pytest.mark.negative
# def test_unknown_link(update_refresh_token):
#     with allure.step("Загрузка файла по неизвестной ссылке на Google Drive"):
#         value = upload_file(update_refresh_token,
#                             Links.URL_DOWNLOAD, Links.URL_DOWNLOAD)
#     with allure.step("Запрос отправлен, посмотрим код ответа"):
#         assert value.status_code == 400, "Check your link"
