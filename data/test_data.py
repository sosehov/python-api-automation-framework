import json

# For API tests
user_ids = [1, 2, 3]

# For login tests
json_data = '''
[
    {"username": "admin", "password": "123", "expected": "login successful"},
    {"username": "guest", "password": "123", "expected": "invalid credentials"},
    {"username": "admin", "password": "wrongpass", "expected": "invalid credentials"},
    {"username": "testuser", "password": "abc", "expected": "invalid credentials"}
]
'''
login_test_data = json.loads(json_data)