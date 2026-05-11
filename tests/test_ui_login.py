from playwright.sync_api import Page

def test_login_success(page):
  page.goto("https://the-internet.herokuapp.com/login")
  
  page.get_by_label("Username").fill("tomsmith")
  page.get_by_label("Password").fill("SuperSecretPassword!")
  
  page.get_by_role("button", name="Login").click()
  
  success_message = page.get_by_role("alert")
  
  assert success_message.is_visible()
  assert "You logged into a secure area!" in success_message.inner_text()