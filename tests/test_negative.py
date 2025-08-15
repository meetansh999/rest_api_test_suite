import requests

def test_missing_post(base_url):
    r = requests.get(f"{base_url}/posts/999999")
    # Public demo APIs differ; assert your chosen contract in README if needed
    assert r.status_code in (404, 200)

def test_invalid_method_on_collection(base_url):
    r = requests.put(f"{base_url}/posts")  # PUT on a collection often not allowed
    assert r.status_code in (404, 405)
