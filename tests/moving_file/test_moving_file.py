import pytest
from fixtures.moving_file.api import moving_file
import allure
from fixtures.response import Response
from fixtures.constants import Links
from fixtures.add_folder.api import add_new_folder
from fixtures.upload.api import upload_file

@allure.feature("Проверка перемещения файла")
@allure.story("Проверка функции перемещения файла")
@pytest.mark.positive
def test_moving_file(update_refresh_token, get_file_id):
    with allure.step("Перемещение файла на Google Drive"):
        value = moving_file(upload_file(Links.URL_CHECK).json()["id"], add_new_folder(Links.PARENTS).json()["id"])
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 200, "Check your parents ID")

@allure.feature("Проверка перемещения файла")
@allure.story("Проверка функции перемещения файла")
@pytest.mark.negative
def test_moving_unknown_file(update_refresh_token, get_file_id):
    with allure.step("Перемещение несуществующего файла на Google Drive"):
        value = moving_file(Links.FILE_ID, add_new_folder(Links.PARENTS).json()["id"])
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 404, "Check your parents ID")
