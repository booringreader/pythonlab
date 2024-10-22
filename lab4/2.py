# Write a Python program to count the number of occurrences of a given character in a string (Using both inbuilt method and without the inbuilt method).
def count_char_inbuilt(string, char):
    return string.count(char)

def count_char_manual(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count


input_string = input("Enter a string: ")
input_char = input("Enter a character to count: ")

count_inbuilt = count_char_inbuilt(input_string, input_char)
print(f"Occurrences of '{input_char}' using inbuilt method: {count_inbuilt}")

count_manual = count_char_manual(input_string, input_char)
print(f"Occurrences of '{input_char}' using manual method: {count_manual}")
