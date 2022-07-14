import nfc
import binascii
import time
import sqlite3
import db

def readIDm(tag):
    idm = binascii.hexlify(tag.identifier).decode()
    return idm

def connected(tag):
    # IDmを取得
    idm = readIDm(tag)
    print(idm)

    # DBに照合して結果を取得


    # 登録されているIDなら
    ## 入退室情報をDBに記録する

def addMember():
    pass

def main():
    con = sqlite3.connect('main.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    db.init(cur)
    db.User.add(cur, 0, 'さりえり', 0x027e9ed6)
    con.commit()

    users = db.User.getAll(cur)

    for user in users:
        print(user['name'])

    """
    while True:
        with nfc.ContactlessFrontend('usb') as clf:
            clf.connect(rdwr={'on-connect': connected})
        
        time.sleep(1)
    """

if __name__ == '__main__':
    main()
