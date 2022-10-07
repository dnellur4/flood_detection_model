import pytest
from src import main_model 
class test_main():
  def test_predict_main(self):
    assert main_model.main()
  
