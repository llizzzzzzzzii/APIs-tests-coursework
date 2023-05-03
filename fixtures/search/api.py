from fixtures.request import request
from fixtures.constants import Links
from fixtures.deco import logging as log

@log("Search Files")
def search_files(file_name, parents):
    response = request(method="GET",
                       url=Links.URL_CHECK,
                       params={"q": f"name='{file_name}' and '{parents}' in parents"},
                       headers={"Authorization": f"Bearer {Links.ACCESS_TOKEN}"})
    return response