import pytest
from src import main_model 

class test_main():
  def test_predict_main(self):
    d,t =  main_model.main()
    assert isinstance(d,string)
    assert isinstance(t,string)
  
