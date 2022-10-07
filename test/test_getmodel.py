import pytest
from src import App 
from src import main_model
class test_getmodel:
  def test_get_model_app(self):
    assert App.get_model()
  def test_get_model_main(self):
    assert main_model.get_model()
