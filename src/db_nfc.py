import sqlite3
from type_nfc import NfcType
from exception import SqlSyntaxException, NfcNotFoundException

class NfcDb:
    def __init__(self, dbPath: str) -> None:
        con = sqlite3.connect(dbPath)
        con.row_factory = sqlite3.Row

        try:
            self.cur = con.cursor()
            self.cur.execute('CREATE TABLE IF NOT EXISTS NFC(id INTEGER PRIMARY KEY AUTOINCREMENT, nfcId TEXT, userId INTEGER)')
        except sqlite3.Error:
            raise SqlSyntaxException('Could not create "NFC" table.')
    
    def add(self, nfcId: str, userId: int) -> NfcType:
        try:
            self.cur.execute('INSERT INTO NFC(nfcId, userId) values("{0}", {1})'.format(nfcId, userId))
            self.cur.execute('SELECT * FROM NFC WHERE ROWID = last_insert_rowid()')
        except sqlite3.Error:
            raise SqlSyntaxException('Could not add NFC.')
        
        nfcRecord = self.cur.fetchone()
        if nfcRecord == None:
            raise NfcNotFoundException('Could not find NFC.')

        return {
            'id': nfcRecord[0],
            'nfcId': nfcRecord[1],
            'userId': nfcRecord[2]
        }

    def get(self, id: int) -> NfcType | None:
        try:
            self.cur.execute('SELECT * FROM NFC WHERE id = {0}'.format(id))
        except sqlite3.Error:
            raise SqlSyntaxException('Could not get NFC.')
        
        nfcRecord = self.cur.fetchone()
        if nfcRecord == None:
            return None

        return {
            'id': nfcRecord[0],
            'nfcId': nfcRecord[1],
            'userId': nfcRecord[2]
        }

    def getAll(self) -> list[NfcType]:
        try:
            self.cur.execute('SELECT * FROM NFC')
        except sqlite3.Error:
            raise SqlSyntaxException('Could not get NFC.')

        nfcRecordList = self.cur.fetchall()
        nfcList: list[NfcType] = []
        for nfcRecord in nfcRecordList:
            nfcList.append({
                'id': nfcRecord[0],
                'nfcId': nfcRecord[1],
                'userId': nfcRecord[2],
            })

        return nfcRecordList

    def update(self, id: int, nfcId: str, userId: int) -> NfcType | None:
        try:
            self.cur.execute('UPDATE NFC SET nfcId = "{0}", userId = {1} WHERE id = {2}'.format(nfcId, userId, id))
            self.cur.execute('SELECT * FROM NFC WHERE id = {0}'.format(id))
        except sqlite3.Error:
            raise SqlSyntaxException('Could not update NFC.')

        nfcRecord = self.cur.fetchone()
        if nfcRecord == None:
            return None
        
        return {
            'id': nfcRecord[0],
            'nfcId': nfcRecord[1],
            'userId': nfcRecord[2]
        }

    def delete(self, id: int) -> None:
        try:
            self.cur.execute('DELETE FROM NFC WHERE id = {0}'.format(id))
        except sqlite3.Error:
            raise SqlSyntaxException('Could not delete NFC.')