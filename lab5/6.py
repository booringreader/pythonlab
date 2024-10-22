# Write a python program to find the largest word in every line of a text file.

def find_largest_word_in_each_line(file_name):
    try:
        with open(file_name, 'r') as file:
            line_number = 1  # To keep track of the line numbers
            for line in file:
                words = line.strip().split()
                if words:  # Ensure the line has words
                    largest_word = max(words, key=len)
                    print(f"Largest word in line {line_number}: {largest_word}")
                else:
                    print(f"Line {line_number} is empty or contains no words.")
                line_number += 1
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
file_name = input("Enter the file name: ")
find_largest_word_in_each_line(file_name)
            