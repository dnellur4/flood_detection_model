import pytest
from scr.Application.modelprediction import ModelPrediction
import flask

class testModelPrediction:
  def test_get_model(self):
      assert len(ModelPrediction.get_model()) == 2 
  
  def test_get_predictions(self):
      assert ModelPrediction.get_predictions(['There is a flood.', 'Reddit']) == 1 

