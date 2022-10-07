from webapp import client

def test_landing(client):
    landing = client.get("/")
    html = landing.data.decode()
    assert landing.status_code == 200
    # Spot check important text
    assert "Copyright © 2022 - All rights Reserved - Designed by SE-Team15" in html

def test_landing_aliases(client):
    landing = client.get("/")
    assert client.get("/index/").data 

