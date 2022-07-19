import sqlite3
from type_user import UserType

class UserDb:
    def __init__(self, dbPath: str) -> None:
        con = sqlite3.connect(dbPath, isolation_level=None)
        con.row_factory = sqlite3.Row

        self.cur = con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS USERS(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')

    def add(self, name: str) ->  UserType | None:
        self.cur.execute('INSERT INTO USERS(name) values("{0}")'.format(name))
        self.cur.execute('SELECT * FROM USERS WHERE ROWID = last_insert_rowid()')

        for row in self.cur:
            return {
                'id': row[0],
                'name': row[1]
            }

    def get(self, id: int) -> UserType | None:
        self.cur.execute('SELECT * FROM USERS WHERE id = {0}'.format(id))

        for row in self.cur:
            return {
                'id': row[0],
                'name': row[1]
            }

    def getAll(self) -> list[UserType]:
        self.cur.execute('SELECT * FROM USERS')

        users: list[UserType] = []
        for row in self.cur:
            user: UserType = {
                'id': row[0],
                'name': row[1]
            }
            users.append(user)
        
        return users
    
    def set(self, id: int, name: str) -> UserType | None:
        self.cur.execute('UPDATE USERS SET name = "{0}" WHERE id = {1}'.format(name, id))
        self.cur.execute('SELECT * FROM USERS WHERE id = {0}'.format(id))

        for row in self.cur:
            return {
                'id': row[0],
                'name': row[1]
            }

    def delete(self, id: int) -> None:
        self.cur.execute('DELETE FROM USERS WHERE id = {0}'.format(id))