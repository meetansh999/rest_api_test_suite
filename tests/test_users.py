import json
import requests
from jsonschema import Draft7Validator

def load_schema(path="schemas/user.json"):
    with open(path, "r") as f:
        return json.load(f)

def test_users_match_schema(base_url):
    schema = load_schema()
    r = requests.get(f"{base_url}/users")
    assert r.status_code == 200

    data = r.json()
    assert isinstance(data, list) and len(data) > 0

    validator = Draft7Validator(schema)
    for user in data:
        errors = sorted(validator.iter_errors(user), key=lambda e: e.path)
        assert not errors, f"Schema errors: {[e.message for e in errors]}"
