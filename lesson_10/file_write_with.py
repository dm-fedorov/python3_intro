# file_write_with.py
def file_write(file, string):
    try:
        with open(file, 'w') as output_file:
            count = output_file.write(string)
        return count
    except Exception as e:
        return e

if __name__ == '__main__':
    print('записано символов {0}'.format(file_write("top.txt", "Hello!\n")))
