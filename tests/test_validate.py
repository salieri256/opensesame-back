import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/'))

from validate import validateUser

def test_validateUser():
    x = {
        'name': 'Yamada Taro',
        'nfcIdList': ['0123456789abcdef']
    }
    assert validateUser(x)['result'] == True

    x = {
        'name': 'Yamada Taro',
        'nfcIdList': []
    }
    assert validateUser(x)['result'] == True

    x = {}
    assert validateUser(x)['result'] == False

    x = {
        'name': 'Yamada Taro'
    }
    assert validateUser(x)['result'] == False

    x = {
        'nfcIdList': ['0123456789abcdef']
    }
    assert validateUser(x)['result'] == False

    x = {
        'name': '',
        'nfcIdList': []
    }
    assert validateUser(x)['result'] == False

    x = {
        'name': 'Yamada Taro',
        'nfcIdList': ['']
    }
    assert validateUser(x)['result'] == False

    x = {
        'name': None,
        'nfcIdList': []
    }
    assert validateUser(x)['result'] == False

    x = {
        'name': 'Yamada Taro',
        'nfcIdList': None
    }
    assert validateUser(x)['result'] == False

    x = {
        'name': 0,
        'nfcIdList': []
    }
    assert validateUser(x)['result'] == False

    x = {
        'name': 'Yamada Taro',
        'nfcIdList': 0
    }
    assert validateUser(x)['result'] == False

    x = {
        'name': 'Yamada Taro',
        'nfcIdList': ''
    }
    assert validateUser(x)['result'] == False

    x = {
        'name': False,
        'nfcIdList': []
    }
    assert validateUser(x)['result'] == False

    x = {
        'name': 'Yamada Taro',
        'nfcIdList': False
    }
    assert validateUser(x)['result'] == False

    x = {
        'name': {},
        'nfcIdList': []
    }
    assert validateUser(x)['result'] == False

    x = {
        'name': 'Yamada Taro',
        'nfcIdList': {}
    }
    assert validateUser(x)['result'] == False

    x = {
        'name': [],
        'nfcIdList': []
    }
    assert validateUser(x)['result'] == False