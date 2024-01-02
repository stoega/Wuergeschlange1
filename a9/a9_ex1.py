import re

file_name = input("Enter file name: ")
# check if file is valid
try:
    with open(file_name):
        pass
except FileNotFoundError:
    raise ValueError(f"'{input_file}' is not a file")


encoding = input("Enter character encoding or press ENTER for default (utf-8): ")
if encoding == '':
    encoding = 'utf-8'

with open(file_name, encoding=encoding) as file:
    content = file.read()

pattern = input("Enter pattern or press ENTER to exit: ")
while pattern:
    matches = re.findall(pattern, content)
    print(f"{pattern}: {matches}")
    pattern = input("Enter pattern or press ENTER to exit: ")