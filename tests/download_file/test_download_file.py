import pytest
from fixtures.upload.api import upload_file
from fixtures.download.api import download_file
import allure
from fixtures.constants import Links
@allure.feature("Проверка скачивания файла")
@allure.story("Проверка функции скачивания файла 'input.txt' в текущую директорию")
@pytest.mark.positive
def test_download_file(update_refresh_token):
    with allure.step("Скачивание файла с Google Drive"):
        value=download_file(update_refresh_token,upload_file(update_refresh_token,
                                                             Links.URL_DOWNLOAD,Links.URL_CHECK).json()["id"])
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert value.status_code == 200, "Check your file ID"

@allure.feature("Проверка скачивания файла")
@allure.story("Проверка функции скачивания файла 'input.txt' с неизвестным ID в текущую директорию")
@pytest.mark.negative
def test_download_unknown_file(update_refresh_token):
    with allure.step("Скачивание файла по неизвестной ссылке с Google Drive"):
        value=download_file(update_refresh_token,Links.FILE_ID)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert value.status_code == 404, "Check your file ID"