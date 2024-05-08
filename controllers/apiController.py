import json

import requests

from config import API_PORT, API_IP
from models.Tank import Tank

API_URL = f"http://{API_IP}:{API_PORT}/api/"


def auth(login, passwd):
    result = requests.get(API_URL + f"auth/login={login}&passwd={passwd}")
    if result.status_code == 200:
        return 1
    elif result.status_code == 401:
        return 0
    elif result.status_code == 500:
        return -1


# def check_admin(login):
#     result = requests.get(API_URL + f"user/check/{login}")
#     if result.status_code == 200:
#         return result.json()["admin"]
#     return False


def get_tanks():
    # return [
    #     Tank(id=1, name="ЕББ1", type_id=1),
    #     Tank(id=2, name="ЕТБ1", type_id=2),
    #     Tank(id=3, name="ЕТБ2", type_id=2),
    # ]
    result = requests.get(API_URL + f"tanks")
    return result.json()


# async def get_tank_info_ws(tank_id):
#     return websockets.connect(f"ws://localhost:5000/api/tank/{tank_id}/ws")


# def get_current_temperature(tank_id):
#     return np.random.normal()
#
#
# def get_current_tank_state(tank_name):
#     pass

if __name__ == '__main__':
    pass