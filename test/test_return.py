import pytest
from src import App
import flask

class test_app:
    def test_return_app(self):
        assert isinstance(App.return_app(), flask.Flask) 
