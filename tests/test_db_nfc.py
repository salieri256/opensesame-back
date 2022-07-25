import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/'))

import sqlite3
from db import NfcDb

def test_db_nfc_init():
    dbPath = 'test_db_nfc_init.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)

    NfcDb(dbPath)

    con = sqlite3.connect(dbPath)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    nfcTableNum = cur.execute('SELECT COUNT(*) FROM sqlite_master WHERE TYPE="table" AND name="NFC"').fetchone()[0]

    assert nfcTableNum == 1

def test_db_nfc_add():
    dbPath = 'test_db_nfc_add.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    nfcDb = NfcDb(dbPath)

    nfcId = ''
    userId = 0
    nfc = nfcDb.add(nfcId, userId)
    if nfc == None:
        assert False

    assert nfc['nfcId'] == nfcId
    assert nfc['nfcId'] == nfcId

def test_db_nfc_get():
    dbPath = 'test_db_nfc_get.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    nfcDb = NfcDb(dbPath)

    nfc1 = nfcDb.add('', 0)
    if nfc1 == None:
        assert False
    
    nfc2 = nfcDb.get( nfc1['id'] )
    if nfc2 == None:
        assert False
    
    assert nfc1['id'] == nfc2['id']
    assert nfc1['nfcId'] == nfc2['nfcId']
    assert nfc1['userId'] == nfc2['userId']

def test_db_nfc_get_not_exist():
    dbPath = 'test_db_nfc_get_not_exist.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    nfcDb = NfcDb(dbPath)

    nfc = nfcDb.get(0)
    assert nfc == None

def test_db_nfc_getAll():
    dbPath = 'test_db_nfc_getAll.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    nfcDb = NfcDb(dbPath)

    nfcDb.add('', 0)
    nfcDb.add('', 0)

    nfcList = nfcDb.getAll()
    assert len(nfcList) == 2

def test_db_nfc_update():
    dbPath = 'test_db_nfc_set.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    nfcDb = NfcDb(dbPath)

    nfc1 = nfcDb.add('012345', 0)
    if nfc1 == None:
        assert False

    nfc2 = nfcDb.update( nfc1['id'], 'abcdef', 1 )
    if nfc2 == None:
        assert False
    
    assert nfc1['id'] == nfc2['id']
    assert nfc2['nfcId'] == 'abcdef'
    assert nfc2['userId'] == 1

def test_db_nfc_update_not_exist():
    dbPath = 'test_db_nfc_set_not_exist.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    nfcDb = NfcDb(dbPath)

    nfc = nfcDb.update(0, 'abcdef', 1)
    assert nfc == None

def test_db_nfc_delete():
    dbPath = 'test_db_nfc_delete.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    nfcDb = NfcDb(dbPath)

    nfc1 = nfcDb.add('', 0)
    if nfc1 == None:
        assert False

    nfcDb.delete(nfc1['id'])

    nfc2 = nfcDb.get(nfc1['id'])
    assert nfc2 == None

def test_db_nfc_delete_not_exist():
    dbPath = 'test_db_nfc_delete_not_exist.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    nfcDb = NfcDb(dbPath)

    nfcDb.delete(0)

    nfc = nfcDb.get(0)
    assert nfc == None