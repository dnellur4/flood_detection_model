import pytest
from src import App
from src import main_model
import flask

class test_getmodel:
  def test_get_model_app(self):
      assert isinstance(App.get_model(), flask.Flask) == True
  def test_get_model_main(self):
    assert isinstance(main_model.get_model(), flask.Flask) == True
