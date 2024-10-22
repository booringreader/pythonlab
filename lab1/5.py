input = int(input("Enter the number of days: "))
days = input

years = input // 365 
weeks = float(float(days%365) // 7)

print(f"{days} days is equal to {years} year(s) and {weeks} week(s).")