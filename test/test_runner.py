import pytest
from test import runner 
import flask
class test_runner():
  def test_runner_init(self):
    assert isinstance(runner(),flask.Flask.test_cli_runner()) == True
