# Write a Python program to read first n lines of a file from a text file.

def read_first_n_lines(file_name, n):
    try:
        with open(file_name, 'r') as file:
            for i in range(n):
                line = file.readline()  
                if not line:
                    print("End of file reached.")
                    break
                print(line.strip()) 
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

file_name = input("Enter the file name: ")
n = int(input("Enter the number of lines to read: "))

read_first_n_lines(file_name, n)
