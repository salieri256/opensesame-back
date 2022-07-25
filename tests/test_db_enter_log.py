import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/'))

import sqlite3
from db import EnterLogDb

def test_db_enter_log_init():
    dbPath = 'test_db_enter_log_init.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)

    EnterLogDb(dbPath)

    con = sqlite3.connect(dbPath)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    enterLogTableNum = cur.execute('SELECT COUNT(*) FROM sqlite_master WHERE TYPE="table" AND name="ENTERLOG"').fetchone()[0]

    assert enterLogTableNum == 1

def test_db_enter_log_add():
    dbPath = 'test_db_enter_log_add.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    enterDb = EnterLogDb(dbPath)

    entered = 0
    unixTime = 0
    userId = 0
    enterLog = enterDb.add(entered, unixTime, userId)
    if enterLog == None:
        assert False

    assert enterLog['entered'] == entered
    assert enterLog['unixTime'] == unixTime
    assert enterLog['userId'] == userId

def test_db_enter_log_get():
    dbPath = 'test_db_enter_log_get.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    enterDb = EnterLogDb(dbPath)

    enter1 = enterDb.add(0, 0, 0)
    if enter1 == None:
        assert False
    
    enter2 = enterDb.get( enter1['id'] )
    if enter2 == None:
        assert False
    
    assert enter1['id'] == enter2['id']
    assert enter1['entered'] == enter2['entered']
    assert enter1['unixTime'] == enter2['unixTime']
    assert enter1['userId'] == enter2['userId']

def test_db_enter_log_get_not_exist():
    dbPath = 'test_db_enter_log_get_not_exist.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    enterDb = EnterLogDb(dbPath)

    enter = enterDb.get(0)
    assert enter == None

def test_db_enter_log_getAll():
    dbPath = 'test_db_enter_log_getAll.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    enterDb = EnterLogDb(dbPath)

    enterDb.add(0, 0, 0)
    enterDb.add(0, 0, 0)

    enterList = enterDb.getAll()
    assert len(enterList) == 2

def test_db_enter_log_update():
    dbPath = 'test_db_enter_log_set.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    enterDb = EnterLogDb(dbPath)

    enter1 = enterDb.add(0, 0, 0)
    if enter1 == None:
        assert False

    enter2 = enterDb.update( enter1['id'], 1, 1000, 1 )
    if enter2 == None:
        assert False
    
    assert enter1['id'] == enter2['id']
    assert enter2['entered'] == 1
    assert enter2['unixTime'] == 1000
    assert enter2['userId'] == 1

def test_db_enter_log_update_not_exist():
    dbPath = 'test_db_enter_log_set_not_exist.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    enterDb = EnterLogDb(dbPath)

    enter = enterDb.update(0, 0, 0, 0)
    assert enter == None

def test_db_enter_log_delete():
    dbPath = 'test_db_enter_log_delete.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    enterDb = EnterLogDb(dbPath)

    enter1 = enterDb.add(0, 0, 0)
    if enter1 == None:
        assert False

    enterDb.delete(enter1['id'])

    enter2 = enterDb.get(enter1['id'])
    assert enter2 == None

def test_db_enter_log_delete_not_exist():
    dbPath = 'test_db_enter_log_delete_not_exist.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    enterDb = EnterLogDb(dbPath)

    enterDb.delete(0)

    enter = enterDb.get(0)
    assert enter == None