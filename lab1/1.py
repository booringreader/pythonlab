principal = float(input("Enter the principal amount: ")) 
rate = float(input("Enter the rate of interest (in %): ")) 
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100

print(f"earned interest: {simple_interest}")