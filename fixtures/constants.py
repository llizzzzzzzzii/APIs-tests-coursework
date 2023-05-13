import os

class Links:
    CLIENT_ID = "77864409271-ujcgeg2243mca6ek98pn7qahbjjhalga." \
                "apps.googleusercontent.com"
    CLIENT_SECRET = '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'
    REDIRECT_URI = 'http://localhost:8080'
    SCOPE = 'https://www.googleapis.com/auth/drive'
    REFRESH_TOKEN = '1//' \
                    '0c_QMjblQzhrECgYIARAAGAwSNwF-L9Ir8BdP8rZPXUf07o0a6OQHbLbIsX8wjRvuC4YzHp007JB0s42CdFhTYjFOJRHVIGgUgRM'
    GET_TOKEN = 'https://accounts.google.com/o/oauth2/auth?'
    TOKEN_URL = 'https://oauth2.googleapis.com/token'
    # ссылка по которой загружаем файл
    URL_DOWNLOAD = "https://www.googleapis.com/upload/" \
                   "drive/v3/files?uploadType=multipart"
    FILE_PATH = os.path.join(os.path.abspath("")[: os.path.abspath("").find('py-pytest') + 10], "data/input.txt")
    FILE_NAME = "input.txt"
    PARENTS = "1Geg7D6y-7wueDGxoGFFtDfvjrVUDTVwr"
    # некорректный ID который используем для негативных тестов
    FILE_ID = 'WEn4zGvB7fCo0Ew6WYJpL2KPhH'
    # ссылка чтобы сделать действия с определенным файлом, после / обычно пишем ID файла
    URL_CHECK = "https://www.googleapis.com/drive/v3/files/"
    AUTH_URL = 'https://accounts.google.com/o/oauth2/auth?client_id={}&' \
               'redirect_uri={}&scope=https://www.googleapis.com/' \
               'auth/drive&response_type=code&access_type=offline'
    # файл в который записываем содержимое скачанного файла
    DOWNLOAD_FILE_NAME = os.path.join(os.path.abspath("")[: os.path.abspath("").find('py-pytest') + 10], "data/downloaded_file.txt")
    ACCESS_TOKEN = 'ya29.a0AWY7CkktLKzfQbNTDx2dp9R6CCQH7K1C14WOPHPXSQlkmKr0COMMnM6hMpLJSOvwleerIZV8t10NIU4N-mVp4xDovbattKX9IGwMdIUKQBMrJ88p4OuWP80V5bkv0dCA8aRcPEBmdXlrtCnFppi1vlSFN5dyLX5CaCgYKAYESAQ4SFQG1tDrpH8r9Kf3fDrnDPosJhoWbZw0167'
    FILE_ID_CORR = '1QZX7KDqQn3B9wqkDnGIJt4twph51K9wb'
    # для негативных тестов
    FILE_NAME_INCORR = 'input.txt'
    # для негативных тестов
    PARENTS_INCORR = 'D6y-7wueDGxoGFFtDfvjrVUDTVwr'
    # файл который скачиваем, он всегда один
    DOWNLOAD_FILE_ID = '1aR5wXYRFi-KO8AE-6WQdrUJHG_W-QRXm'
    # новое название файла на которое будет переименовывать существующий файл
    NEW_FILE_NAME = 'testikk.txt'
    # имя папки которую будем создавать
    FOLDER_NAME = 'test_folder'
    # такая же ссылка как и URL_CHECK, только без / в конце
    URL_ADD = 'https://www.googleapis.com/drive/v3/files'
    # ссылка для редактирования содержимого файла
    URL_UPLOAD = 'https://www.googleapis.com/upload/drive/v3/files/'
    # ID файла у которого будем менять содержимое файла
    EDIT_FILE_ID = '1ij2QoKNmpRV4XXYN6hs9lZr8BifCcAH6'
    # ID файла у которого будем получать дату и размер
    ID_FILE = '1ZSaMSuxncc210cJRdVwGb-VCO4Bi_7Sl'
    # папка которую будем искать
    NAME_FOLDER = 'python'
    # дата создания файла у которого будем получать размер и дату
    DATE = '2023-05-04T06:57:36.763Z'
    # имя файла который будем создавать
    CREATE_FILE_NAME = 'creating file.txt'
    # ID папки в которую будем перемещать файл
    FOLDER_FOR_MOVING = '1CEJm-UnzfaNjcYQKW7Ctjx1d5S-DO44V'
    # ссылка по которой перемещаем файл в корзину
    URL_DELETE = 'https://www.googleapis.com/drive/v2/files/'
    # тип файла который будем загружать
    MIMETYPE='text/plain'