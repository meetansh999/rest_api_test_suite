import requests

def test_service_reachable(base_url):
    r = requests.get(f"{base_url}/posts")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    