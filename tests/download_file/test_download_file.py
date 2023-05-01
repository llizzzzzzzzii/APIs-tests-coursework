
import pytest
from fixtures.upload.api import upload_file
from fixtures.download.api import download_file
import allure

@allure.feature("Проверка скачивания файла")
@allure.story("Проверка функции скачивания файла 'input.txt' в текущую директорию")
@pytest.mark.positive
def test_download_file(update_refresh_token):
    value=download_file(update_refresh_token,upload_file(update_refresh_token,Links.URL_DOWNLOAD,Links.URL_CHECK).json()["id"])
    assert value.status_code == 200, "Check your file ID"