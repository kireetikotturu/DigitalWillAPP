# auth.py
import os

USER_FILE = "data/users.txt"

def register(username, password):
    if not os.path.exists(USER_FILE):
        open(USER_FILE, 'w').close()

    with open(USER_FILE, "r") as file:
        for line in file:
            user, _ = line.strip().split(",")
            if user == username:
                return False, "User already exists."

    with open(USER_FILE, "a") as file:
        file.write(f"{username},{password}\n")
    return True, "Registration successful."

def login(username, password):
    if not os.path.exists(USER_FILE):
        return False, "No users found."

    with open(USER_FILE, "r") as file:
        for line in file:
            user, pwd = line.strip().split(",")
            if user == username and pwd == password:
                return True, "Login successful."
    return False, "Invalid credentials."
