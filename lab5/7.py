# Write a Python Program to traverse all the files in a folder (path given by the user), and print the lines and the name of file containing the substring “NIT”
import os
def find_nit_in_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    # Read each line in the file
                    for line_number, line in enumerate(f, start=1):
                        # Check if the substring "NIT" is in the current line
                        if "NIT" in line:
                            print(f"Found in {file_path}, Line {line_number}: {line.strip()}")
            except Exception as e:
                # Handle files that cannot be opened (like binary files)
                print(f"Could not read file {file_path}: {e}")
folder_path = input("Enter the folder path: ")
find_nit_in_files(folder_path)
