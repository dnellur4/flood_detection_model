from webapp import client
class test_predict_page():
    def test_predict(self,client):
        landing = client.get("/predict")
        html = landing.data.decode()
        assert landing.status_code == 200
        # Spot check important text
        assert "Copyright © 2022 - All rights Reserved - Designed by SE-Team15" in html

    def test_predict_aliases(self,client):
        landing = client.get("/predict")
        assert client.get("/predict/").data 
