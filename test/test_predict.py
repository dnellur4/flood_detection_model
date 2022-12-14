from test import client


def test_predict(client):
    landing = client.get("/predict")
    assert landing.status_code == 200
    # Spot check important text
    assert "Copyright © 2022 - All rights Reserved - Designed by SE-Team15" in landing.data.decode(
    )


def test_predict_aliases(client):
    landing = client.get("/predict")
    assert client.get("/predict/").data
