import pytest
from src import main_model 
class Predict:
    def test_predict_flood(self):
      assert main_model.predict_flood('There is a flood.', 'Reddit') == 1
      assert main_model.predict_flood('All the streets of the city are filled with flood water', 'Twitter') == 1

    def test_predict_no_flood(self):
      assert main_model.predict_flood('The agricultural lands in are filled with large volumes of rain water.', 'Instagram') == 0
      assert main_model.predict_flood('sea has water', 'Instagram') == 0
