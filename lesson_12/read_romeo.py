# read_romeo.py
def read_url(url):
    import urllib.request
    try:
        with urllib.request.urlopen(url) as webpage:
            text = webpage.read().decode('utf-8')
        return text
    except Exception as e: 
        return e

if __name__ == "__main__":    
    print(read_url("http://dfedorov.spb.ru/python3/src/romeo.txt"))
