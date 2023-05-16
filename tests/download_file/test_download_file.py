import pytest
from fixtures.download.api import download_file
import allure
from fixtures.constants import Links
from fixtures.response import Response
from com.jsonschema.error import ResponseError404

@allure.feature("Проверка скачивания файла")
@allure.story("Проверка функции скачивания файла 'input.txt'")
@pytest.mark.positive
def test_download_file(update_refresh_token):
    with allure.step("Скачивание файла с Google Drive"):
        value = download_file(Links.DOWNLOAD_FILE_ID)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 200, "Check your file ID")

# @allure.feature("Проверка скачивания файла")
# @allure.story("Проверка функции скачивания файла 'input.txt' с неизвестным ID")
# @pytest.mark.negative
# def test_download_unknown_file(update_refresh_token):
#     with allure.step("Скачивание файла по неизвестной ссылке с Google Drive"):
#         value = download_file(Links.FILE_ID)
#     with allure.step("Запрос отправлен, проверим тело ответа"):
#         Response.validate(value, ResponseError404.schema)
#     with allure.step("Запрос отправлен, посмотрим код ответа"):
#         Response.log_assert(value.status_code == 404, "Check your file ID")

