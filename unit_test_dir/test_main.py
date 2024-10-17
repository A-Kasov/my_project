from fastapi.testclient import TestClient
import os, sys

sys.path.append(os.path.dirname(os.getcwd()))
from main import app



client = TestClient(app)

def test_read_root():
    print('Hello')
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
