import binascii
import nfc
import time

import httpx

DB_SERVICE_BASE_URL = 'http://127.0.0.1:8001'
DB_SERVICE_USERS_PATH = '/users'
DB_SERVICE_DOORS_PATH = '/doors'
DB_SERVICE_LOCK_PATH = '/doors/{}/lock'
DB_SERVICE_LOCK_LOGS_PATH = '/logs/locks'
DOOR_LOCK_BASE_URL = 'http://127.0.0.1:8000'
DOOR_LOCK_LOCK_PATH = '/lock'
DOOR_ID = 1

def convert_bytes_to_id(data: bytes):
    idm = binascii.hexlify(data)
    return idm.decode()

def fetch_users():
    res = httpx.get(DB_SERVICE_BASE_URL + DB_SERVICE_USERS_PATH)
    users = res.json()
    return users

def fetch_doors():
    res = httpx.get(DB_SERVICE_BASE_URL + DB_SERVICE_DOORS_PATH)
    door = res.json()
    return door

def lock_door():
    httpx.post(DOOR_LOCK_BASE_URL + DOOR_LOCK_LOCK_PATH)

def unlock_door():
    httpx.delete(DOOR_LOCK_BASE_URL + DOOR_LOCK_LOCK_PATH)

def keep_door_lock(doorId: int):
    httpx.post(DB_SERVICE_BASE_URL + DB_SERVICE_LOCK_PATH.format(doorId))

def keep_door_unlock(doorId: int):
    httpx.delete(DB_SERVICE_BASE_URL + DB_SERVICE_LOCK_PATH.format(doorId))

def post_lock_log(doorId: int, userId: int, isLocked: bool):
    lock_log_base_body = {
        'doorId': doorId,
        'userId': userId,
        'isLocked': isLocked,
    }
    httpx.post(DB_SERVICE_BASE_URL + DB_SERVICE_LOCK_LOGS_PATH, json=lock_log_base_body)

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
    
    for door in doors:
        if door['id'] == DOOR_ID:
            on_found_door_with_same_door_id(user, door)

def on_detect_nfc(tag: nfc.tag.Tag):
    nfcId = convert_bytes_to_id(tag.identifier)
    users = fetch_users()

    print(nfcId)

    for user in users:
        if user['nfcId'] == nfcId:
            on_found_user_with_same_nfc(user)

def main():
    try:
        while True:
            with nfc.ContactlessFrontend('usb') as clf:
                clf.connect(rdwr={'on-connect': on_detect_nfc})
                time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()