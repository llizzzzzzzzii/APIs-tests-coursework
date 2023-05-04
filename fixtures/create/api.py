from fixtures.constants import Links
from fixtures.request import Request
def create_file(parents):
    response = Request("Create new file").send_request(method="POST",
                                                      url=f"{Links.URL_ADD}",
                                                      headers={'Authorization': f'Bearer {Links.ACCESS_TOKEN}'},
                                                      json={'name': Links.CREATE_FILE_NAME,
                                                            'parents': [parents]})
    return response

