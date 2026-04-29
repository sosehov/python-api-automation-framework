def login(username, password):
    if username == "admin" and password == "123":
        return "login successful"
    return "invalid credentials"