# read_romeo2.py
def read_url(url):
    import urllib.request    
    with urllib.request.urlopen(url) as webpage:
        text = webpage.read().decode('utf-8')
    return text
    
if __name__ == "__main__":    
    try:
        print(read_url("http://dfedorov.spb.ru/python3/src/romeo.txt"))
    except Exception as e:
        print(e)
