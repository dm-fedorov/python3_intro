# file_reader_with_plan_for.py
def file_reader(file):
    result = dict()
    try:
        with open(file, 'r') as file:
            for line in file:                
                result[line] = len(line.strip())
        return result
    except Exception as e:
        return e
        
if __name__ == '__main__':
    print(file_reader('plan.txt'))
