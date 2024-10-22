# Write a Python program to calculate the length of a string (using both inbuilt method and without using the inbuilt method).

def length_using_len(input_string):
    return len(input_string)

input_string = input("input: ")
print("Length of the string using len():", length_using_len(input_string))



def length_without_len(input_string):
    count = 0
    for character in input_string:
        count += 1
    return count

input_string =input("input: ")
print("Length of the string without using len():", length_without_len(input_string))
