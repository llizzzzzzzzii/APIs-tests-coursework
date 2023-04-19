import json
import os
import requests
from constants import Links
from com.automation.example.refresh_new_token import *
from com.automation.example.upload_func import *
def test_upload_file():
    value=upload_file(Links.FILE_NAME)
    assert value.status_code == 200
    assert value.json().get('name') == Links.FILE_NAME
