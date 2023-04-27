from conftest import *
import pytest
from fixtures.upload.api import *

@pytest.mark.positive
def test_upload_file(update_refresh_token):
    value = upload_file(update_refresh_token,Links.URL_DOWNLOAD,Links.URL_CHECK)
    assert value.status_code == 200, 'Check your file ID or file name'
    assert value.json().get('name') == Links.FILE_NAME, 'Check your file ID or file name'


@pytest.mark.negative
def test_unknown_link(update_refresh_token):
    value = upload_file(update_refresh_token, Links.URL_DOWNLOAD,Links.URL_DOWNLOAD)
    assert value.status_code == 400, "Check your link"
