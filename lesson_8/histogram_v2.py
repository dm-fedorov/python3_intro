# histogram_v2.py
def histogram(s):
    '''
    Функция для подсчета встречаемости элементов в коллекции s.
    '''
    word_count = {}
    for word in s:
        word_count.setdefault(word, 0)  # word_count[key] = 0, если такого key не было ранее
        word_count[word] += 1 # word_count[word] = word_count[word] + 1        
    return word_count

if __name__ == "__main__":
    print(histogram("sdfs"))
    print(histogram(['aaa', 'bbb', 'aaa', 'bbb', 'c']))
