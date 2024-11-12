import re

def is_valid_email(email):
    # Regular expression pattern for validating email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

email = input("check validity of email: ")
if is_valid_email(email):
    print("The email is valid.")
else:
    print("The email is invalid.")
