import re

def find_emails(text):
    # Regular expression pattern for finding email addresses
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, text)
    return emails

# Example usage
text = input("contact details: ")
emails = find_emails(text)
print("Found emails:", emails)
