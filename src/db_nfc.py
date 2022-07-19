import sqlite3
from type_nfc import NfcType

class NfcDb:
    def __init__(self, dbPath: str) -> None:
        con = sqlite3.connect(dbPath)
        con.row_factory = sqlite3.Row

        self.cur = con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS NFC(id INTEGER PRIMARY KEY AUTOINCREMENT, nfcId TEXT, userId INTEGER)')
    
    def add(self, nfcId: str, userId: int) -> NfcType | None:
        self.cur.execute('INSERT INTO NFC(nfcId, userId) values("{0}", {1})'.format(nfcId, userId))
        self.cur.execute('SELECT * FROM NFC WHERE ROWID = last_insert_rowid()')

        for row in self.cur:
            return {
                'id': row[0],
                'nfcId': row[1],
                'userId': row[2]
            }

    def get(self, id: int) -> NfcType | None:
        self.cur.execute('SELECT * FROM NFC WHERE id = {0}'.format(id))

        for row in self.cur:
            return {
                'id': row[0],
                'nfcId': row[1],
                'userId': row[2]
            }

    def getAll(self) -> list[NfcType]:
        self.cur.execute('SELECT * FROM NFC')

        nfcIdList: list[NfcType] = []
        for row in self.cur:
            nfcId: NfcType = {
                'id': row[0],
                'nfcId': row[1],
                'userId': row[2]
            }
            nfcIdList.append(nfcId)
        
        return nfcIdList

    def set(self, id: int, nfcId: str, userId: int) -> NfcType | None:
        self.cur.execute('UPDATE NFC SET nfcId = "{0}", userId = {1} WHERE id = {2}'.format(nfcId, userId, id))
        self.cur.execute('SELECT * FROM NFC WHERE id = {0}'.format(id))

        for row in self.cur:
            return {
                'id': row[0],
                'nfcId': row[1],
                'userId': row[2]
            }

    def delete(self, id: int) -> None:
        self.cur.execute('DELETE FROM NFC WHERE id = {0}'.format(id))