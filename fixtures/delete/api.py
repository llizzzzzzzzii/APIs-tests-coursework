import requests
from fixtures.constants import Links
from fixtures.deco import logging as log

@log("Delete file")
def delete_file(update_refresh_token,file_id):
    access_token=update_refresh_token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    url = f"{Links.URL_CHECK}{file_id}"
    response = requests.delete(url, headers=headers)
    return response

