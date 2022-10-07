from webapp import client
def test_predict(client):
    landing = client.get("/login_socialmedia")
    html = landing.data.decode()
    assert landing.status_code == 200
    # Spot check important text
    assert "Copyright © 2022 - All rights Reserved - Designed by SE-Team11" in html

def test_predict_aliases(client):
    landing = client.get("/login_socialmedia")
    assert client.get("/login_socialmedia/").data 
