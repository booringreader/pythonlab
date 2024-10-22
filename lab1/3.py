a = input("Enter the value of a: ") 
b = input("Enter the value of b: ")

temp=a; a=b; b=temp;
print(f"After swapping:\na = {a}\nb = {b}")