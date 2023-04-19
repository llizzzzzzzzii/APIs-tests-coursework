# import allure
# import time
# from allure_commons.types import AttachmentType
# from selenium import webdriver
#
# exec_path = 'GoogleDriveSetup.exe'
#
# class TestPageSearch:
#     def setup(self):
#         self.driver = webdriver.Chrome(executable_path=exec_path)
#
#     def teardown(self):
#         self.driver.quit()
#
# #@Feature — аннотация, размещаемая над тестом. Позволяет группировать тесты по проверяемому функционалу.
# #@Story — аннотация, размещаемая над тестом. Позволяет группировать тесты по User story.
# #@Severity — аннотация, размещаемая над тестом. Позволяет указать уровень критичности функционала, проверяемого автотестом.
#     #Данная аннотация принимает параметр «value», который может быть одним из
#     # элементов enum SeverityLevel: BLOCKER, CRITICAL, NORMAL, MINOR или TRIVIAL.
#     @allure.feature('Open page')
#     @allure.story('Открываем страницу google drive')
#     @allure.severity('blocker')
#     def test_google_search(self):
#         self.driver.get('https://drive.google.com/drive/my-drive')
#         with allure.step('Делаем скриншот'):
#             allure.attach(self.driver.get_screenshot_as_png(), name='Screen', attachment_type=AttachmentType.PNG)
#         assert self.driver.title == 'Google Диск: вход в систему'
#
#
