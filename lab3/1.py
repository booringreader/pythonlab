# WAP to convert binary number taken as user input into its decimal equivalent

input = str(input("enter binary number: ")) # raw_input() returns string
exponent=0
for digit in input:
    exponent = exponent*2 + int(digit)
print("output: ", exponent)

# logic of LCM, we keep dividing the number by 2 and the remainder becomes binary code
# reverse that logic and the multiplication by 2 then adding the remainder makes it easier to track the number from left to right