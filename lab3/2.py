def binary_to_decimal(binary_str, index=0):
    if index == len(binary_str):
        return 0

    
    current_bit_value = int(binary_str[index]) * (2 ** (len(binary_str) - 1 - index))
    

    return current_bit_value + binary_to_decimal(binary_str, index + 1)

binary_str = input("Enter a binary number: ")

decimal_value = binary_to_decimal(binary_str)

print(f"The decimal equivalent of binary {binary_str} is {decimal_value}")
