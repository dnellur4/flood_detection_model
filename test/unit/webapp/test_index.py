from webapp import client
class test_index_page():
    def test_landing(self,client):
        landing = client.get("/")
        html = landing.data.decode()
        assert landing.status_code == 200
        # Spot check important text
        assert "Copyright © 2022 - All rights Reserved - Designed by SE-Team15" in html

    def test_landing_aliases(self,client):
        landing = client.get("/")
        assert client.get("/index/").data 

