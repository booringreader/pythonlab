from collections import Counter 

string = str(input("input string: "))
count = Counter(string)

print("number of vowels: ", (count['a'] + count['e'] + count['i'] + count['o'] + count['u']))

# vowels with '' turn into accents