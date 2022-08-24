import binascii
import nfc
import time

import httpx

DB_SERVICE_BASE_URL = 'http://127.0.0.1:8001'
USERS_RESOURCE_PATH = '/users'
ACTIVE_RESOURCE_PATH = '/users/{}/active'
ACTIVITY_LOGS_RESOURCE_PATH = '/logs/activities'

def convert_bytes_to_id(data: bytes):
    idm = binascii.hexlify(data)
    return idm.decode()

def fetch_users():
    res = httpx.get(DB_SERVICE_BASE_URL + USERS_RESOURCE_PATH)
    users = res.json()
    return users

def activate_user(userId: int):
    httpx.post(DB_SERVICE_BASE_URL + ACTIVE_RESOURCE_PATH.format(userId))

def deactivate_user(userId: int):
    httpx.delete(DB_SERVICE_BASE_URL + ACTIVE_RESOURCE_PATH.format(userId))

def post_activity_log(userId: int, isActive: bool):
    activity_log_base_body = {
        'userId': userId,
        'isActive': isActive,
    }
    httpx.post(DB_SERVICE_BASE_URL + ACTIVITY_LOGS_RESOURCE_PATH, json=activity_log_base_body)

def on_found_user_with_same_nfc(user: dict):
    userId = user['id']
    if user['isActive'] == False:
        activate_user(userId)
        post_activity_log(userId, True)
    else:
        deactivate_user(userId)
        post_activity_log(userId, False)

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