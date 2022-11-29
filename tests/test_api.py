import requests


def test_insert():
    r = requests.get('http://localhost:3001/admin/insert')
    assert r.status_code == 200


def test_select():
    r = requests.get('http://localhost:3001')
    assert r.status_code == 200


def test_delete():
    r = requests.get('http://localhost:3001/admin/delete')
    assert r.status_code == 200
