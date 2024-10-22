# Given the decimal number 168, represent it using octal and hexadecimal literals

decimal_number = 168

# octal
octal_number = oct(decimal_number)

# hexadecimal
hexadecimal_number = hex(decimal_number)


print(f"Decimal: {decimal_number}")
print(f"Octal: {octal_number[2:]}")
print(f"Hexadecimal: {hexadecimal_number[2:].upper()}")
