import requests
from config import API_PORT, API_IP

API_URL = f"http://{API_IP}:{API_PORT}/api/"


def auth(login, passwd):
    result = requests.get(API_URL + f"auth/login={login}&passwd={passwd}")
    if result.status_code == 200:
        return 1
    elif result.status_code == 401:
        return 0
    elif result.status_code == 500:
        return -1


def get_tanks():
    result = requests.get(API_URL + f"tanks")
    return result.json()


def activate_tank(tank_id, user_login):
    result = requests.get(API_URL + f"process/start/tank={tank_id}&user={user_login}")


def emergency_stop(tank_id, user_login):
    result = requests.get(API_URL + f"process/stop/tank={tank_id}&user={user_login}")
