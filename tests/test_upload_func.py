from com.automation.example.upload_func import *
from fixtures.constants import *
from conftest import *

def test_upload_file(update_refresh_token):
    value = upload_file(update_refresh_token)
    assert value.status_code == 200, 'Check your file ID or file name'
    assert value.json().get('name') == Links.FILE_NAME, 'Check your file ID or file name'
