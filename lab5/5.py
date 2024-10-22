# Write a program to count no. of characters and no. of words in a text file.

def count_characters_and_words(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            num_of_characters = len(content)
            words = content.split()
            num_of_words = len(words)
            
            print(f"The file {file_name} has {num_of_characters} characters and {num_of_words} words.")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

file_name = input("Enter the file name: ")
count_characters_and_words(file_name)
