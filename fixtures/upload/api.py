from fixtures.request import Request
from fixtures.constants import Links

def upload_file(url_check):
        response = Request("Upload new file").send_request(method="GET",
                           url=f"{url_check}{Links.FILE_ID_CORR}",
                           headers={"Authorization": f"Bearer {Links.ACCESS_TOKEN}"})
        return response
