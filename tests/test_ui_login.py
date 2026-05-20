import pytest
from utils.pages.login_page import LoginPage
from data.ui_login_data import valid_login, invalid_logins

def test_login_success(page):
  login_page = LoginPage(page)
  
  login_page.navigate()
  login_page.login(valid_login["username"], valid_login["password"])
  login_page.assert_success

@pytest.mark.parametrize("user", invalid_logins)
def test_login_failure(page, user):
  login_page = LoginPage(page)
  
  login_page.navigate()
  login_page.login(user["username"], user["password"])
  
  login_page.assert_error