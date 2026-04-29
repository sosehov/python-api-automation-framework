import pytest
from utils.login_utils import login
from data.test_data import users


@pytest.mark.parametrize("user", users)
def test_login(user):
    result = login(user["username"], user["password"])
    assert result == user["expected"]
