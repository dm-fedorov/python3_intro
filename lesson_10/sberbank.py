# sberbank.py
def money_reader(what, where, when):
    """
    Функция возвращает некоторый показатель по сведениям Сбербанка в выбранном городе за указанный период.

    what - что ищем, например 'Средняя зарплата'.
    where - где ищем, например 'Санкт-Петербург'.
    when - когда ищем, указываем год.
    
    """
    import csv
    money = list()
    try:
        with open('opendata.csv', encoding='cp1251') as csvfile:
            money_reader = csv.reader(csvfile) # delimiter по умолчанию ','
            for row in money_reader:
                if row[0] == what:
                    if row[1] == where:                    
                        lst = row[2].split('-')                    
                        if lst[0] == when:                    
                            money.append(int(row[3]))
        return round(sum(money)/len(money), 2)     
    except Exception as e:
        return e

if __name__ == '__main__':

    print('Санкт-Петербург')
    for year in range(2015, 2019):
        print(str(year), money_reader('Средняя зарплата', 'Санкт-Петербург', str(year)))

    print('Москва')
    for year in range(2015, 2019):
        print(str(year), money_reader('Средняя зарплата', 'Москва', str(year)))        
 
