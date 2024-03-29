import requests

API_URL = "http://127.0.0.1:8000/api/"


def auth(login, passwd):
    result = requests.get(API_URL + f"auth/{login}&{passwd}")
    return result.status_code == 200
