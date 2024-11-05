import re

def find_script_tags(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if re.match(r'^\s*<script', line):  # Match lines starting with <script
                    print(line.strip())
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")

file_name = "webpage.md" 
find_script_tags(file_name)
