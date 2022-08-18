import binascii
import nfc

def onConnected(tag):
    idm = binascii.hexlify(tag.identifier)
    id_str = idm.decode()
    print(id_str)

def main():
    clf = nfc.ContactlessFrontend('usb')
    clf.connect(rdwr={'on-connected': onConnected})
    clf.close()

if __name__ == '__main__':
    main()