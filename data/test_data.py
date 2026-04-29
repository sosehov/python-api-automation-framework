import json

json_data = '''
[
    {"username": "admin", "password": "123", "expected": "login successful"},
    {"username": "guest", "password": "123", "expected": "invalid credentials"},
    {"username": "admin", "password": "wrongpass", "expected": "invalid credentials"},
    {"username": "testuser", "password": "abc", "expected": "invalid credentials"}
]
'''

users = json.loads(json_data)