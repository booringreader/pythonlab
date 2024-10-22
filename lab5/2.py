# WAP to demonstrate the use of seek(), get(), closed, etc.

with open("test.txt", "w") as f:
    f.write("NIT Srinagar\n")
    f.write("This is an example file.\n")

with open("test.txt", "r") as f:
    content = f.read(10)
    print("First 10 characters:", content)
    
    f.seek(0)
    print("\nAfter seek(0), the file pointer is reset to:", f.tell())
    
    first_line = f.readline()
    print("First line:", first_line.strip())
    
    f.seek(5)
    print("\nAfter seek(5), the file pointer is at:", f.tell())
    
    more_content = f.read(5)
    print("Next 5 characters after seek(5):", more_content)
    print("\nIs the file closed? (before closing):", f.closed)
print("Is the file closed? (after closing):", f.closed)
