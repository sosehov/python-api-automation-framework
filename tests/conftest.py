import pytest

@pytest.fixture(scope="session")
def headers():
  return {
    "x-api-key": "pub_df5264ffcb16458c69576063a787b925355301f0f0c61a9eaea89e1ea6c3eb44",
    "Content-Type": "application/json"
  }

@pytest.fixture(scope="session")
def base_url():
  return "https://reqres.in/api"

@pytest.fixture(scope="session", autouse=True)
def setup_environment():
  print("\n[SETUP] Starting test session")
  
  yield
  
  print("\n[TEARDOWN] Ending test session")

@pytest.fixture(scope="function")
def fresh_user_payload():
  return {
    "user": "so",
    "job": "QA Engineer"
    }
