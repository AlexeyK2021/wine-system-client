import numpy as np
import requests

from config import API_PORT, API_IP, LOGIN_AS

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


def get_current_temperature(tank_id):
    return np.random.normal()


def get_current_pressure(tank_id):
    pass


def get_current_sensors_state(tank_id):
    pass


def get_current_actuators_state(tank_id):
    pass
