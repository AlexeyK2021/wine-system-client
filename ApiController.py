import requests

API_IP = "127.0.0.1"
API_URL = f"http://{API_IP}:5000/api/"


def set_ip(ip):
    global API_IP
    API_IP = ip


def auth(login, passwd):
    result = requests.get(API_URL + f"auth/{login}&{passwd}")
    return result.status_code == 200


def check_admin(login):
    result = requests.get(API_URL + f"auth/user/{login}")
    if result.status_code == 200:
        return result.json()["admin"]
    return False
