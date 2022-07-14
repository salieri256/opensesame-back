from sqlite3 import Cursor

def init(cur: Cursor):
    User.init()
    cur.execute('CREATE TABLE IF NOT EXISTS LOG(id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)')

class User:
    def init(cur: Cursor):
        cur.execute('CREATE TABLE IF NOT EXISTS USERS(id INTEGER, name TEXT, isIn INTEGER, nfcId INTEGER)')

    def add(cur: Cursor, id: int, name: str, isIn: bool, nfcID: int):
        cur.execute('INSERT INTO USERS(id, name, isIn, nfcId) values({0}, "{1}", {2}, {3})'.format(id, name, isIn, nfcID))

    def delete(cur: Cursor, id: int):
        cur.execute('DELETE FROM USERS WHERE id = {0}'.format(id))
    
    def set(cur: Cursor, id: int, name: str, isIn: bool, nfcId: int):
        pass

    def get(cur: Cursor, id: int):
        pass

    def getAll(cur: Cursor):
        cur.execute('SELECT * FROM USERS')

        users = [{int, str, int}]

        for user in cur:
            users.append(user)
        
        return users

class Door:
    def init(cur: Cursor):
        pass

    def get(cur: Cursor):
        return 0
    
    def set(cur: Cursor, isLocked: bool):
        return 0

