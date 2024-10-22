# WAP to print the ASCII value of all the characters in a string

from collections import Counter

string = str(input("input string: "))
for i in string:
    print("ASCII value of ", i , ": ", ord(i))
