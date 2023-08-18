# test_hello.py
from main import app

def test_main():
    os.environ["ENVIRONMENT"] = "dev"
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello dev!'