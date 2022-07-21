import sqlite3
from exception import SqlSyntaxException, UserNotFoundException
from type_user import UserType

class UserDb:
    def __init__(self, dbPath: str) -> None:
        con = sqlite3.connect(dbPath, isolation_level=None)
        con.row_factory = sqlite3.Row

        try:
            self.cur = con.cursor()
            self.cur.execute('CREATE TABLE IF NOT EXISTS USERS(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
        except sqlite3.Error:
            raise SqlSyntaxException('Could not create "USERS" table.')

    def add(self, name: str) -> UserType:
        try:
            self.cur.execute('INSERT INTO USERS(name) values("{0}")'.format(name))
        except sqlite3.Error:
            raise SqlSyntaxException('Could not insert user.')

        try:
            self.cur.execute('SELECT * FROM USERS WHERE ROWID = last_insert_rowid()')
        except sqlite3.Error:
            raise SqlSyntaxException('Could not select user.')

        user = self.cur.fetchone()
        if user == None:
            raise UserNotFoundException('Could not found user.')

        return {
            'id': user[0],
            'name': user[1]
        }

    def get(self, id: int) -> UserType | None:
        try:
            self.cur.execute('SELECT * FROM USERS WHERE id = {0}'.format(id))
        except sqlite3.Error:
            raise SqlSyntaxException('Could not select user.')
        
        user = self.cur.fetchone()
        if user == None:
            return None
        
        return {
            'id': user[0],
            'name': user[1]
        }

    def getAll(self) -> list[UserType]:
        try:
            self.cur.execute('SELECT * FROM USERS')
        except sqlite3.Error:
            raise SqlSyntaxException('Could not select users.')

        users = self.cur.fetchall()
        return users
    
    def update(self, id: int, name: str) -> UserType:
        try:
            self.cur.execute('UPDATE USERS SET name = "{0}" WHERE id = {1}'.format(name, id))
        except sqlite3.Error:
            raise SqlSyntaxException('Could not update user.')
        
        try:
            self.cur.execute('SELECT * FROM USERS WHERE id = {0}'.format(id))
        except sqlite3.Error:
            raise SqlSyntaxException('Coud not select user.')
        
        user = self.cur.fetchone()
        if user == None:
            raise UserNotFoundException('Could not found user.')
        
        return {
            'id': user[0],
            'name': user[1]
        }

    def delete(self, id: int) -> None:
        try:
            self.cur.execute('DELETE FROM USERS WHERE id = {0}'.format(id))
        except sqlite3.Error:
            raise SqlSyntaxException('Could not delete user.')