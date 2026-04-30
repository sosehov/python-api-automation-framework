from utils.api_client import get_user, create_user
from data.test_data import user_ids
import pytest

''' Another way to send the API key in the header
headers = {
  "Authorization": "Bearer pub_df5264ffcb16458c69576063a787b925355301f0f0c61a9eaea89e1ea6c3eb44",
  "Content-Type": "application/json"
}
'''

# using parametrization
@pytest.mark.parametrize("user_ids", user_ids)
def test_get_multiple_users(base_url, headers, user_ids):
    response = get_user(base_url, headers, user_ids)
    data = response.json()

    assert response.status_code == 200
    assert data["data"]["id"] == user_ids
    

# parametrize with expected values
@pytest.mark.parametrize("user_ids,expected_id", [
    (1, 1),
    (2, 2),
    (3, 3),
])
def test_user_ids(base_url, headers, user_ids, expected_id):
    response = get_user(base_url, headers, user_ids)
    data = response.json()

    assert response.status_code == 200
    assert data["data"]["id"] == expected_id


def test_create_user(base_url, headers):
    payload = {
        "name": "So",
        "job": "QA Engineer"
    }

    response = create_user(base_url, headers, payload)
    data = response.json()

    assert response.status_code == 201
    assert data["name"] == "So"
    assert data["job"] == "QA Engineer"
    assert isinstance(data.get("id"), str)


@pytest.mark.parametrize("user_ids", [9999])
def test_user_not_found(base_url, headers, user_ids):
    response = get_user(base_url, headers, user_ids)

    assert response.status_code == 404