import binascii

def onConnected(tag):
    idm = binascii.hexlify(tag.identifier)
    id_str = idm.decode()
    print(id_str)