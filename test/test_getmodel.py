import pytest
from src import App 
class test_getmodel:
  def test_get_model(self):
    assert App.get_model()
