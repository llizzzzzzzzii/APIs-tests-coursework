import os
import pytest
import requests
from google.oauth2.credentials import Credentials
def test_upload_file_to_drive(test_file):
    file_path = os.path.join(os.getcwd(),test_file)

    # Получение токена авторизации
    credentials = Credentials.from_authorized_user_info(info={'access_token': 'ya29.a0Ael9sCPqGq3yW5p4swizZGpuvLB1Qmacie4LnEpcI664ZIEg0aK_OTTd4WjQ8ARKdf8AK5FneDacj-sR0b8VWKWWXDDu50nbyr4M3uTP1BKGRtBdc3DZf1q3IRgsNJJ_eyAQSFo3t8dVnvNxj8YHn2m83czdaCgYKAcMSARISFQF4udJhRA_LnIAeJfQ27DQAeJMpvQ0163',
                                                              'refresh_token': 'ya29.a0Ael9sCPqGq3yW5p4swizZGpuvLB1Qmacie4LnEpcI664ZIEg0aK_OTTd4WjQ8ARKdf8AK5FneDacj-sR0b8VWKWWXDDu50nbyr4M3uTP1BKGRtBdc3DZf1q3IRgsNJJ_eyAQSFo3t8dVnvNxj8YHn2m83czdaCgYKAcMSARISFQF4udJhRA_LnIAeJfQ27DQAeJMpvQ0163',
                                                              # 'refresh_token': '1//04r787uASzED9CgYIARAAGAQSNwF-L9Ir-C74zltx2F5Fes7cEys10nU1j5FH_d4Tp1X1sbSVfbahEW2LbZpOIiaL4Ti_1je6N8E',
                                                              'client_id': '77864409271-ujcgeg2243mca6ek98pn7qahbjjhalga.apps.googleusercontent.com',
                                                              'client_secret': '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',
                                                              'token_uri': 'https://oauth2.googleapis.com/token'})
    headers = {
        'Authorization': f"Bearer {credentials.token}",
        'Content-Type': 'application/octet-stream'
    }

    url = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=media'

    with open(file_path, 'rb') as file:
        data = file.read()
    response = requests.post(url, headers=headers, data=data)
    return response

