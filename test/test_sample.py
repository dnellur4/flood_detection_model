import pytest
from src.main_model import *
class Predict:
    def test_predict_flood(self):
      assert predict_flood('There is a flood.', 'Reddit') == 1
    
    def test_predict_no_flood(self):
      assert predict_flood('The agricultural lands in are filled with large volumes of rain water.', 'Instagram') == 0
