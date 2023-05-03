from fixtures.request import Request
from fixtures.constants import Links

def search_files(file_name, parents):
    response = Request("Search Files").send_request(method="GET",
                       url=Links.URL_CHECK,
                       params={"q": f"name='{file_name}' and '{parents}' in parents"},
                       headers={"Authorization": f"Bearer {Links.ACCESS_TOKEN}"})
    return response