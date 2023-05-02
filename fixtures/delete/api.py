from fixtures.request import request
from fixtures.constants import Links
from fixtures.deco import logging as log

@log("Delete file")
def delete_file(file_id):
    response = request(method="DELETE",
                       url=f"{Links.URL_CHECK}{file_id}",
                       headers={"Authorization": f"Bearer {Links.ACCESS_TOKEN}"})
    return response

