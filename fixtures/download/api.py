# from fixtures.upload.api import *
# from fixtures.constants import *
# from fixtures.deco import logging as log
#
# @log("Download file")
#
# def download_file(update_refresh_token,file_id):
#     access_token=update_refresh_token
#     url = f'{Links.URL_CHECK}{file_id}?alt=media'
#     headers = {
#         "Authorization": f"Bearer {access_token}"
#     }
#     response = requests.get(url, headers=headers)
#
#     with open(Links.DOWNLOAD_FILE_NAME, 'wb') as f:
#         f.write(response.content)
#
#     return response