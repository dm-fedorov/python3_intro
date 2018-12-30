# file_reader_with.py
def read_file(file):
    try:
        with open(file, 'r') as file:
            contents = file.read()
        return contents
    except Exception as e:
        return e

if __name__ == '__main__':
    print(read_file('example_text.txt'))


