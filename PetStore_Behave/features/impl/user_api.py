import requests
from PetStore_Behave.features.config import settings
import time

def post_user(payload):
    url = f"{settings.base_url}/user/createWithList"
    return requests.post(url, json=payload)

def get_user(username):
    url = f"{settings.base_url}/user/{username}"
    time.sleep(3)
    return requests.get(url)

def put_user(username, data):
    url = f"{settings.base_url}/user/{username}"
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, json=data, headers=headers)
    return response

def delete_user(username):
    url = f"{settings.base_url}/user/{username}"
    time.sleep(3)
    return requests.delete(url)