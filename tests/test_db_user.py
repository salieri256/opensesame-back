import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/'))

import sqlite3
from db import UserDb

def test_db_user_init():
    dbPath = 'test_db_user_init.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)

    UserDb(dbPath)

    con = sqlite3.connect(dbPath)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    userTableNum = cur.execute('SELECT COUNT(*) FROM sqlite_master WHERE TYPE="table" AND name="USER"').fetchone()[0]

    assert userTableNum == 1

def test_db_user_add():
    dbPath = 'test_db_user_add.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    userDb = UserDb(dbPath)

    userName = 'test'
    user = userDb.add(userName)
    if user == None:
        assert False

    assert user['name'] == userName

def test_db_user_get():
    dbPath = 'test_db_user_get.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    userDb = UserDb(dbPath)

    user1 = userDb.add('test')
    if user1 == None:
        assert False
    
    user2 = userDb.get( user1['id'] )
    if user2 == None:
        assert False
    
    assert user1['id'] == user2['id']
    assert user1['name'] == user2['name']

def test_db_user_get_not_exist():
    dbPath = 'test_db_user_get_not_exist.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    userDb = UserDb(dbPath)

    user = userDb.get(0)
    if user == None:
        assert True
    else:
        assert False

def test_db_user_getAll():
    dbPath = 'test_db_user_getAll.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    userDb = UserDb(dbPath)

    userDb.add('test1')
    userDb.add('test2')

    userList = userDb.getAll()
    assert len(userList) == 2

def test_db_user_update():
    dbPath = 'test_db_user_set.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    userDb = UserDb(dbPath)

    user1 = userDb.add('Alice')
    if user1 == None:
        assert False

    user2 = userDb.update( user1['id'], 'Bob' )
    if user2 == None:
        assert False
    
    assert user1['id'] == user2['id']
    assert user2['name'] == 'Bob'

def test_db_user_update_not_exist():
    dbPath = 'test_db_user_set_not_exist.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    userDb = UserDb(dbPath)

    user = userDb.update(0, 'test')
    if user == None:
        assert True
    else:
        assert False

def test_db_user_delete():
    dbPath = 'test_db_user_delete.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    userDb = UserDb(dbPath)

    user1 = userDb.add('test')
    if user1 == None:
        assert False

    userDb.delete(user1['id'])

    user2 = userDb.get(user1['id'])
    if user2 == None:
        assert True
    else:
        assert False

def test_db_user_delete_not_exist():
    dbPath = 'test_db_user_delete_not_exist.db'

    if os.path.isfile(dbPath):
        os.remove(dbPath)
    
    userDb = UserDb(dbPath)

    userDb.delete(0)

    user = userDb.get(0)
    if user == None:
        assert True
    else:
        assert False