import re

def find_mobile_numbers(text):
    # Regular expression pattern for finding mobile numbers (assuming 10-digit format)
    pattern = r'\b[6-9][0-9]{9}\b'
    mobile_numbers = re.findall(pattern, text)
    return mobile_numbers

mobile_numbers = find_mobile_numbers(input("text:"))
print("Found mobile numbers:", mobile_numbers)
