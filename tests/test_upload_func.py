import pytest
from com.automation.example.upload_func import *
def test_upload():
    value=upload('input')
    assert value.status_code==200
    assert value.json().get('name')=='input'