import client
def test_predict(client):
    landing = client.get("/predict")
    html = landing.data.decode()
    assert landing.status_code == 200
    # Spot check important text
    assert "Copyright © 2022 - All rights Reserved - Designed by SE-Team11" in html

def test_predict_aliases(client):
    landing = client.get("/predict")
    assert client.get("/predict/").data 
