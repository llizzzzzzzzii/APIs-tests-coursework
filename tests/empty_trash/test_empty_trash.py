import pytest
from fixtures.constants import Links
from fixtures.empty_trash.api import empty_trash
import allure
from fixtures.response import Response

@allure.feature("Проверка очистки корзины")
@allure.story("Проверка функции очистки корзины")
@pytest.mark.positive
def test_empty_trash(update_refresh_token):
    with allure.step("Очистка корзины Google Drive"):
        value = empty_trash(Links.URL_DELETE)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 204, "Check your URL")

@allure.feature("Проверка очистки корзины")
@allure.story("Проверка функции очистки корзины по непраивльной ссылке")
@pytest.mark.negative
def test_fail_empty_trash(update_refresh_token):
    with allure.step("Очистка корзины по неправильной ссылке на Google Drive"):
        value = empty_trash(Links.URL_DOWNLOAD)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        Response.log_assert(value.status_code == 400, "Check your URL")
