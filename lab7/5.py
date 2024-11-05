import re

def find_ip_addresses(text):
    # Regular expression pattern for IP addresses
    pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    ips = re.findall(pattern, text)
    return ips

ips = find_ip_addresses(input("text: "))
print("Found IP addresses:", ips)
