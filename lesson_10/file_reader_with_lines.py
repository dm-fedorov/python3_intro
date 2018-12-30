# file_reader_with_lines.py
def file_reader(file):
    try:
        with open(file, 'r') as file:
            lines = file.readlines()
        return lines
    except Exception as e:
        return e

if __name__ == '__main__':    
    print(file_reader('example_text.txt'))
    
