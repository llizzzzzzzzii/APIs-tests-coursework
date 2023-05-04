from fixtures.constants import Links
from fixtures.request import Request

def moving_file(file_id, new_parents):
    response = Request("Moving file").send_request(method="PATCH",
                                                   url=f'https://www.googleapis.com/drive/v3/files/{file_id}?'
                                                       f'addParents={new_parents}&removeParents={Links.PARENTS}',
                                                   headers={'Authorization': f'Bearer {Links.ACCESS_TOKEN}',
                                                            'Content-Type': 'application/json'})
    return response
