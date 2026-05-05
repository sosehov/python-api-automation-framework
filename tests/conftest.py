from dotenv import load_dotenv
import os
import pytest

load_dotenv()

@pytest.fixture(scope="session")
def headers():
  api_key = os.getenv("API_KEY")
  assert api_key is not None, "API_KEY is not set"
  
  return {
    "x-api-key": api_key,
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
