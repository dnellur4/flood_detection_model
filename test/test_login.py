from test import client
def test_predict(client):
    landing = client.get("/login_socialmedia")
    assert landing.status_code == 200 


def test_predict_aliases(client):
    landing = client.get("/login_socialmedia")
    assert client.get("/login_socialmedia/").data  != None
