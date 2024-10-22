# WAP to find factorial of a number using Iteration

output = 1
for i in range(1, int(input("input n: "))+1):
    output *= i

print("output: ", output)

# if range() is passed with one argument, python starts from 0
# use range(start, range) where start is the start of indexing
# range(num) is exclusive of num
