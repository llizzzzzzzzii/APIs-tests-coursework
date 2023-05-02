from fixtures.deco import logging as log
from fixtures.request import request
from fixtures.constants import Links

@log("Upload new file")
def upload_file(url_check):
        response = request(method="GET",
                           url=f"{url_check}{Links.FILE_ID_CORR}",
                           headers={"Authorization": f"Bearer {Links.ACCESS_TOKEN}"})
        return response
