import sqlite3
from exception import SqlSyntaxException, UserNotFoundException
from type_user import UserType

class UserDb:
    def __init__(self, dbPath: str) -> None:
        con = sqlite3.connect(dbPath, isolation_level=None)
        con.row_factory = sqlite3.Row

        try:
            self.cur = con.cursor()
            self.cur.execute('CREATE TABLE IF NOT EXISTS USER(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
        except sqlite3.Error:
            raise SqlSyntaxException('Could not create "USER" table.')

    def add(self, name: str) -> UserType:
        try:
            self.cur.execute('INSERT INTO USER(name) values("{0}")'.format(name))
            self.cur.execute('SELECT * FROM USER WHERE ROWID = last_insert_rowid()')
        except sqlite3.Error:
            raise SqlSyntaxException('Could not add user.')

        userRecord = self.cur.fetchone()
        if userRecord == None:
            raise UserNotFoundException('Could not find user.')

        return {
            'id': userRecord[0],
            'name': userRecord[1]
        }

    def get(self, id: int) -> UserType | None:
        try:
            self.cur.execute('SELECT * FROM USER WHERE id = {0}'.format(id))
        except sqlite3.Error:
            raise SqlSyntaxException('Could not get user.')
        
        userRecord = self.cur.fetchone()
        if userRecord == None:
            return None
        
        return {
            'id': userRecord[0],
            'name': userRecord[1]
        }

    def getAll(self) -> list[UserType]:
        try:
            self.cur.execute('SELECT * FROM USER')
        except sqlite3.Error:
            raise SqlSyntaxException('Could not get users.')

        userRecordList = self.cur.fetchall()
        userList: list[UserType] = []
        for userRecord in userRecordList:
            userList.append({
                'id': userRecord[0],
                'name': userRecord[1]
            })

        return userList
    
    def update(self, id: int, name: str) -> UserType | None:
        try:
            self.cur.execute('UPDATE USER SET name = "{0}" WHERE id = {1}'.format(name, id))
            self.cur.execute('SELECT * FROM USER WHERE id = {0}'.format(id))
        except sqlite3.Error:
            raise SqlSyntaxException('Coud not update user.')
        
        userRecord = self.cur.fetchone()
        if userRecord == None:
            return None
        
        return {
            'id': userRecord[0],
            'name': userRecord[1]
        }

    def delete(self, id: int) -> None:
        try:
            self.cur.execute('DELETE FROM USER WHERE id = {0}'.format(id))
        except sqlite3.Error:
            raise SqlSyntaxException('Could not delete user.')