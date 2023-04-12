import os
import json
import requests
def upload(filename):
    f_path=os.path.join(os.getcwd(),filename)
    with open(f_path,"w") as file:
        file.write("testttt")
    headers={"Authorization":"Bearer ???"}
    parametr={"name":'input', "parents":["???"]}
    files={"data":("metadata",json.dumps(parametr),"application/json;charset=UTF-8"),
           "file":open(f_path,"rb")}
    url = "https://www.googleapis.com/upload/drive/v3/files"
    r=requests.post(url,headers=headers,files=files)
    return r