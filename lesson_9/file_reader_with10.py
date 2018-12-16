# file_reader_with10.py
with open('example_text.txt', 'r') as file:
    contents = file.read(10)
    rest = file.read()

print("10:", contents)
print("остальное:", rest)
