from test import client


def test_landing(client):
    landing = client.get("/")
    assert landing.status_code == 200
    assert "Copyright © 2022 - All rights Reserved - Designed by SE-Team15" in landing.data.decode(
    )


def test_landing_aliases(client):
    landing = client.get("/")
    assert client.get("/index/").data
