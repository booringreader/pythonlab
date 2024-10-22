def is_palindrome(number):
    original_str = str(number)
    reversed_str = original_str[::-1]
    return original_str == reversed_str

num = int(input("Enter an integer: "))
    
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")