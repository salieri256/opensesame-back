import nfc
import binascii

def connected(tag):
    idm = binascii.hexlify(tag.identifier)
    idstr = idm.decode()
    print(idstr)

clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected}) # now touch a tag
clf.close()