import pytest
from Application.App import *  

@pytest.fixture
def client():
    flask_app = return_app()
    flask_app.config['TESTING'] = True
    client = flask_app.test_client()

    yield client

@pytest.fixture()
def runner(flask_app):
    return flask_app.test_cli_runner()
