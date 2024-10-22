# WAP to fetch all the lines starting with Word “NIT” from a text file.
def fetch_lines_starting_with_NIT(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith('NIT'):
                    print(line.strip())  # Print the line without extra newlines
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

filename = 'test.txt'  # Replace with the name of your file
fetch_lines_starting_with_NIT(filename)
