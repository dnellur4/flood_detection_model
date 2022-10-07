import pytest
from src import App 

@pytest.fixture
def client():
    flask_app = App.return_app()
    flask_app.config['TESTING'] = True
    client = flask_app.test_client()

    yield client

@pytest.fixture()
def runner(flask_app):
    return flask_app.test_cli_runner()
