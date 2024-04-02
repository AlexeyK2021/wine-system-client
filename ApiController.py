import requests

from config import API_PORT, API_IP

API_URL = f"http://{API_IP}:{API_PORT}/api/"


def auth(login, passwd):
    result = requests.get(API_URL + f"auth/{login}&{passwd}")
    return result.status_code == 200


def check_admin(login):
    result = requests.get(API_URL + f"user/check/{login}")
    if result.status_code == 200:
        return result.json()["admin"]
    return False
