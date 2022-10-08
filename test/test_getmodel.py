import pytest
from src.App import * 
from src.main_model import *
class test_getmodel:
  def test_get_model_app(self):
      return App.get_model()
  def test_get_model_main(self):
    assert main_model.get_model()
