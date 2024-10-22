# Write a Python Program to traverse all the sub-directories and sub-files present in them to extract text file names containing the substring “NIT”.
import os
def find_nit_files(start_directory):
    nit_files = []
    
    for dirpath, dirnames, filenames in os.walk(start_directory):
        for filename in filenames:
            if 'NIT' in filename and filename.endswith('.txt'):
                full_path = os.path.join(dirpath, filename)
                nit_files.append(full_path)
    return nit_files
start_directory = input("path to file: ")
nit_text_files = find_nit_files(start_directory)
print("Text files containing 'NIT':")
for file in nit_text_files:
    print(file)
