import pytest
from utils.login_utils import login
from data.test_data import login_test_data


@pytest.mark.parametrize("user", login_test_data)
def test_login(user):
    result = login(user["username"], user["password"])
    assert result == user["expected"]
