# Write a Program to count no. of lines in a text file.
def count_lines_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            num_of_lines = len(lines)
            print(f"The file {file_name} has {num_of_lines} lines.")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

file_name = input("Enter the file name: ")
count_lines_in_file(file_name)
