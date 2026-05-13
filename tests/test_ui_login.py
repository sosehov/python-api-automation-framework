import pytest
from utils.pages.login_page import LoginPage

def test_login_success(page):
  login_page = LoginPage(page)
  
  login_page.navigate()
  login_page.login("tomsmith", "SuperSecretPassword!")
  login_page.assert_success

@pytest.mark.parametrize("username, password", [
  ("wronguser", "SuperSecretPassword!"),
  ("tomsmith", "wrongpass"),
  ])
def test_login_failure(page, username, password):
  login_page = LoginPage(page)
  
  login_page.navigate()
  login_page.login(username, password)
  
  login_page.assert_error