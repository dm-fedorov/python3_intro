# file_reader.py
def file_reader(path):    
    try:        
        file = open(path, 'r')
        contents = file.read()
        file.close()
        return contents
    except Exception as e:
        return e
    
if __name__ == '__main__':
    print(file_reader('example_text.txt'))
