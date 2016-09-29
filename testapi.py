import requests
from requests.auth import HTTPBasicAuth


playlod = {"username": "sssssssssss",
           "email": "sssssss@ss.com", "is_staff": "false"}

url = "http://45.116.168.137:8000/users/"
r = requests.post(url, auth=HTTPBasicAuth(
    'root', 'gaoyan940320'), data=playlod)
print r.text
