import os
import pytest
import requests
from google.oauth2.credentials import Credentials
def test_upload_file_to_drive(test_file):
    file_path = os.path.join(os.getcwd(),test_file)

    # Получение токена авторизации
    credentials = Credentials.from_authorized_user_info(info={'access_token': 'ya29.a0Ael9sCMLY0OcCy-471KE0n25ywFGKq8gC_mRZJBIhST9x9XguHqX-uwBLQprQNVERReCbpcSD9PQRAsq_0ibLbaINjkSDGCrE_MCwE48D-syeZTefSF52_W5l3V67Gfv88vRnDI55q9FsVgubTR0BOSdukRgaCgYKAUUSARISFQF4udJhyjU_slB_qxA91wPQLhLAiw0163',
                                                              'refresh_token': 'ya29.a0Ael9sCMLY0OcCy-471KE0n25ywFGKq8gC_mRZJBIhST9x9XguHqX-uwBLQprQNVERReCbpcSD9PQRAsq_0ibLbaINjkSDGCrE_MCwE48D-syeZTefSF52_W5l3V67Gfv88vRnDI55q9FsVgubTR0BOSdukRgaCgYKAUUSARISFQF4udJhyjU_slB_qxA91wPQLhLAiw0163',
                                                              # 'refresh_token': '1//04qEH7eV1Cj9bCgYIARAAGAQSNwF-L9IrgHKkvHxdsKOtb5mtCWCAh3VDQXmiBmk2jdPfNnhM8v6cdjFjB9V0_k3fwDR34v8zFp0',
                                                              'client_id': '77864409271-ujcgeg2243mca6ek98pn7qahbjjhalga.apps.googleusercontent.com',
                                                              'client_secret': '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',
                                                              'token_uri': 'https://oauth2.googleapis.com/token'})
    headers = {
        'Authorization': f"Bearer {credentials.refresh_token}",
        'Content-Type': 'application/json; charset=utf-8'
    }

    url = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=media'

    with open(file_path, 'rb') as file:
        data = file.read()
    response = requests.post(url, headers=headers, data=data)
    return response

