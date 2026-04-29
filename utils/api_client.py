import requests

def get_user(base_url, headers, user_id):
  return requests.get(
    f"{base_url}/users/{user_id}",
    headers=headers
  )
  
def login(username, password):
  if username == "admin" and password == "123":
      return "login successful"
  return "invalid credentials"

def create_user(base_url, headers, payload):
  return requests.post(f"{base_url}/users", json=payload, headers=headers)