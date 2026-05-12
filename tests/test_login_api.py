import requests
import pytest

@pytest.mark.parametrize("payload, expected_status", [
  ({"email": "eve.holt@reqres.in", "password": "cityslicka"}, 200),
  ({"email": "peter@klaven"}, 400),
])
def test_login_api(base_url, headers, payload, expected_status):
  response = requests.post(
    f"{base_url}/login",
    json=payload,
    headers=headers
  )
  
  assert response.status_code == expected_status
  
  if response.status_code == 200:
    data=response.json()
    assert "token" in data
    assert isinstance(data["token"], str)