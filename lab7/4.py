import re

def check_password_strength(password):
    # Check if password is at least 8 characters
    if len(password) < 8:
        return "Password too short, must be 8 characters or more."

    # Check for special characters
    if not re.search(r'[\W_]', password):  # \W matches any non-word character
        return "Password must contain at least one special character."

    return "Password is strong."

# Example usage
password = input("Enter a password: ")
print(check_password_strength(password))
