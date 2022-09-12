import os
import binascii
import nfc
import time

import httpx

DB_SERVICE_BASE_URL = os.environ['DB_SERVICE_BASE_URL']
DB_SERVICE_USERS_PATH = '/users'
DB_SERVICE_DOORS_PATH = '/doors'
DB_SERVICE_LOCK_PATH = '/doors/{}/lock'
DB_SERVICE_LOCK_LOGS_PATH = '/logs/locks'
DOOR_LOCK_BASE_URL = os.environ['DOOR_LOCK_BASE_URL']
DOOR_LOCK_LOCK_PATH = '/lock'
DEVICE_PATH = os.environ['DEVICE_PATH']
DOOR_ID = int( os.environ['DOOR_ID'] )

def convert_bytes_to_id(data: bytes):
    idm = binascii.hexlify(data)
    return idm.decode()

def fetch_users():
    try:
        res = httpx.get(DB_SERVICE_BASE_URL + DB_SERVICE_USERS_PATH)
        users = res.json()
        return users
    except Exception as e:
        print(e)
        return None

def fetch_doors():
    try:
        res = httpx.get(DB_SERVICE_BASE_URL + DB_SERVICE_DOORS_PATH)
        door = res.json()
        return door
    except Exception as e:
        print(e)
        return None

def lock_door():
    try:
        httpx.post(DOOR_LOCK_BASE_URL + DOOR_LOCK_LOCK_PATH)
    except Exception as e:
        print(e)

def unlock_door():
    try:
        httpx.delete(DOOR_LOCK_BASE_URL + DOOR_LOCK_LOCK_PATH)
    except Exception as e:
        print(e)

def keep_door_lock(doorId: int):
    try:
        httpx.post(DB_SERVICE_BASE_URL + DB_SERVICE_LOCK_PATH.format(doorId))
    except Exception as e:
        print(e)

def keep_door_unlock(doorId: int):
    try:
        httpx.delete(DB_SERVICE_BASE_URL + DB_SERVICE_LOCK_PATH.format(doorId))
    except Exception as e:
        print(e)

def post_lock_log(doorId: int, userId: int, isLocked: bool):
    lock_log_base_body = {
        'doorId': doorId,
        'userId': userId,
        'isLocked': isLocked,
    }

    try:
        httpx.post(DB_SERVICE_BASE_URL + DB_SERVICE_LOCK_LOGS_PATH, json=lock_log_base_body)
    except Exception as e:
        print(e)

def on_found_door_with_same_door_id(user: dict, door: dict):
    userId = user['id']
    doorId = door['id']

    if door['isLocked'] == False:
        lock_door()
        keep_door_lock(doorId)
        post_lock_log(doorId, userId, True)
    else:
        unlock_door()
        keep_door_unlock(doorId)
        post_lock_log(doorId, userId, False)

def on_found_user_with_same_nfc(user: dict):
    doors = fetch_doors()

    if doors is None:
        return
    
    for door in doors:
        if door['id'] == DOOR_ID:
            on_found_door_with_same_door_id(user, door)

def on_detect_nfc(tag: nfc.tag.Tag):
    nfcId = convert_bytes_to_id(tag.identifier)
    users = fetch_users()

    if users is None:
        return

    for user in users:
        if user['nfcId'] == nfcId:
            on_found_user_with_same_nfc(user)

def main():
    try:
        while True:
            with nfc.ContactlessFrontend(DEVICE_PATH) as clf:
                clf.connect(rdwr={'targets': ['212F', '424F', '106A', '106B'], 'on-connect': on_detect_nfc})
                time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()