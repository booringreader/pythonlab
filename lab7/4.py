import re

def check_password_strength(password):
    if len(password) < 8:
        return "Password too short, must be 8 characters or more."

    if not re.search(r'[\W_]', password):
        return "Password must contain at least one special character."
    return "Password is strong."
password = input("Enter a password: ")
print(check_password_strength(password))
