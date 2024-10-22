def count_elements(s):
    letters = 0
    digits = 0
    special_symbols = 0
    
    for char in s:
        if char.isalpha(): 
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            special_symbols += 1

    return letters, digits, special_symbols

test_string = "Hello123! Welcome @2024."
letters, digits, special_symbols = count_elements(test_string)
print(f"Letters: {letters}") 
print(f"Digits: {digits}")
print(f"Special symbols: {special_symbols}")