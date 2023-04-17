import pytest
from com.automation.example.upload_func import *
def test_upload():
    value=test_upload_file_to_drive('input')
    assert value.status_code==200