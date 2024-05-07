import asyncio
from threading import Thread
from time import sleep

import numpy as np
import requests
import websockets

from config import API_PORT, API_IP, LOGIN_AS
from models.Tank import Tank

API_URL = f"http://{API_IP}:{API_PORT}/api/"


def auth(login, passwd):
    if LOGIN_AS != "":
        return True
    result = requests.get(API_URL + f"auth/login={login}&passwd={passwd}")
    if result.status_code == 200:
        return 1
    elif result.status_code == 401:
        return 0
    elif result.status_code == 500:
        return -1


def check_admin(login):
    if LOGIN_AS == "admin":
        return True
    elif LOGIN_AS == "operator":
        return False
    result = requests.get(API_URL + f"user/check/{login}")
    if result.status_code == 200:
        return result.json()["admin"]
    return False


def get_tanks():
    return [
        Tank(id=1, name="ЕББ1", type_id=1),
        Tank(id=2, name="ЕТБ1", type_id=2),
    ]


# async def get_tank_info_ws(tank_id):
#     return websockets.connect(f"ws://localhost:5000/api/tank/{tank_id}/ws")


# def get_current_temperature(tank_id):
#     return np.random.normal()
#
#
# def get_current_tank_state(tank_name):
#     pass

