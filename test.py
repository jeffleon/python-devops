from werkzeug.wrappers import response
from app import app


def test1():
    response = app.test_client().get('/')
    assert response._status_code == 200

def test2():
    response = app.test_client().get('/edit')
    assert response._status_code == 200

def test3():
    response = app.test_client().get('/edit')
    assert b"To do App" in response.data
    assert b"Todo Title" in response.data