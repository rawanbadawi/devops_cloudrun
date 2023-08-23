# This is how you can test your flask application.
from main import app
import os

def test_main():
    os.environ["ENVIRONMENT"] = "dev"
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello, dev!'