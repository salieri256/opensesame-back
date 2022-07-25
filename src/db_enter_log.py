import sqlite3
from type_enter_log import EnterLogType
from exception import SqlSyntaxException, EnterLogNotFoundException

class EnterLogDb:
    def __init__(self, dbPath: str) -> None:
        con = sqlite3.connect(dbPath)
        con.row_factory = sqlite3.Row

        try:
            self.cur = con.cursor()
            self.cur.execute('CREATE TABLE IF NOT EXISTS ENTERLOG(id INTEGER PRIMARY KEY AUTOINCREMENT, entered INTEGER, unixTime INTEGER, userId INTEGER)')
        except sqlite3.Error:
            raise SqlSyntaxException('Could not create "ENTERLOG" table.')
    
    def add(self, entered: int, unixTime: int, userId: int) -> EnterLogType:
        try:
            self.cur.execute('INSERT INTO ENTERLOG(entered, unixTime, userId) values({0}, {1}, {2})'.format(entered, unixTime, userId))
            self.cur.execute('SELECT * FROM ENTERLOG WHERE ROWID = last_insert_rowid()')
        except sqlite3.Error:
            raise SqlSyntaxException('Cound not add enter log.')
        
        enterLogRecord = self.cur.fetchone()
        if enterLogRecord == None:
            raise EnterLogNotFoundException('Could not find enter log.')

        return {
            'id': enterLogRecord[0],
            'entered': enterLogRecord[1],
            'unixTime': enterLogRecord[2],
            'userId': enterLogRecord[3]
        }

    def get(self, id: int) -> EnterLogType | None:
        try:
            self.cur.execute('SELECT * FROM ENTERLOG WHERE id = {0}'.format(id))
        except sqlite3.Error:
            raise SqlSyntaxException('Could not get enter log.')

        enterLogRecord = self.cur.fetchone()
        if enterLogRecord == None:
            return None

        return {
            'id': enterLogRecord[0],
            'entered': enterLogRecord[1],
            'unixTime': enterLogRecord[2],
            'userId': enterLogRecord[3]
        }

    def getAll(self) -> list[EnterLogType]:
        try:
            self.cur.execute('SELECT * FROM ENTERLOG')
        except sqlite3.Error:
            raise SqlSyntaxException('Could not get enter log.')
        
        enterLogRecordList = self.cur.fetchall()
        enterLogList: list[EnterLogType] = []
        for enterLogRecord in enterLogRecordList:
            enterLogList.append({
                'id': enterLogRecord[0],
                'entered': enterLogRecord[1],
                'unixTime': enterLogRecord[2],
                'userId': enterLogRecord[3]
            })

        return enterLogList

    def update(self, id: int, entered: int, unixTime: int, userId: int) -> EnterLogType | None:
        try:
            self.cur.execute('UPDATE ENTERLOG SET entered = {0}, unixTime = {1}, userId = {2} WHERE id = {3}'.format(entered, unixTime, userId, id))
            self.cur.execute('SELECT * FROM ENTERLOG WHERE id = {0}'.format(id))
        except sqlite3.Error:
            raise SqlSyntaxException('Could not update enter log.')
        
        enterLogRecord = self.cur.fetchone()
        if enterLogRecord == None:
            return None

        return {
            'id': enterLogRecord[0],
            'entered': enterLogRecord[1],
            'unixTime': enterLogRecord[2],
            'userId': enterLogRecord[3]
        }

    def delete(self, id: int) -> None:
        try:
            self.cur.execute('DELETE FROM ENTERLOG WHERE id = {0}'.format(id))
        except sqlite3.Error:
            raise SqlSyntaxException('Could not delete enter log.')