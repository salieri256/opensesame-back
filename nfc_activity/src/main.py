import binascii
import nfc
import time

def convert_bytes_to_id(data: bytes):
    idm = binascii.hexlify(data)
    return idm.decode()

def on_connect(tag: nfc.tag.Tag):
    id = convert_bytes_to_id(tag.identifier)
    print(id)

def main():
    try:
        while True:
            with nfc.ContactlessFrontend('usb') as clf:
                clf.connect(rdwr={'on-connect': on_connect})
                time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()