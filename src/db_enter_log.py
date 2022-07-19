import sqlite3
from type_enter_log import EnterLogType

class EnterLogDb:
    def __init__(self, dbPath: str) -> None:
        con = sqlite3.connect(dbPath)
        con.row_factory = sqlite3.Row

        self.cur = con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS ENTERLOG(id INTEGER PRIMARY KEY AUTOINCREMENT, entered INTEGER, unixTime INTEGER, userId INTEGER)')
    
    def add(self, entered: int, unixTime: int, userId: int) -> EnterLogType | None:
        self.cur.execute('INSERT INTO ENTERLOG(entered, unixTime, userId) values({0}, {1}, {2})'.format(entered, unixTime, userId))
        self.cur.execute('SELECT * FROM ENTERLOG WHERE ROWID = last_insert_rowid()')

        for row in self.cur:
            return {
                'id': row[0],
                'entered': row[1],
                'unixTime': row[2],
                'userId': row[3]
            }

    def get(self, id: int) -> EnterLogType | None:
        self.cur.execute('SELECT * FROM ENTERLOG WHERE id = {0}'.format(id))

        for row in self.cur:
            return {
                'id': row[0],
                'entered': row[1],
                'unixTime': row[2],
                'userId': row[3]
            }

    def getAll(self) -> list[EnterLogType]:
        self.cur.execute('SELECT * FROM ENTERLOG')

        enterLogList: list[EnterLogType] = []
        for row in self.cur:
            enterLog: EnterLogType = {
                'id': row[0],
                'entered': row[1],
                'unixTime': row[2],
                'userId': row[3]
            }
            enterLogList.append(enterLog)
        
        return enterLogList

    def set(self, id: int, entered: int, unixTime: int, userId: int) -> EnterLogType | None:
        self.cur.execute('UPDATE ENTERLOG SET entered = {0}, unixTime = {1}, userId = {2} WHERE id = {3}'.format(entered, unixTime, userId, id))
        self.cur.execute('SELECT * FROM ENTERLOG WHERE id = {0}'.format(id))

        for row in self.cur:
            return {
                'id': row[0],
                'entered': row[1],
                'unixTime': row[2],
                'userId': row[3]
            }

    def delete(self, id: int) -> None:
        self.cur.execute('DELETE FROM ENTERLOG WHERE id = {0}'.format(id))