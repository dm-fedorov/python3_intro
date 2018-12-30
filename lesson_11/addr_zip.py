# addr_zip.py
def print_address(name, line1, line2, city, state, zip1):
    print(name)
    if len(line1) > 0:
        print(line1)
    if len(line2) > 0:
        print(line2)
    print(city + ", " + state + " " + zip1)

# обновленная версия функции
def print_address2(name, line1, line2, city, state, zip1, zip2):
    print(name)
    if len(line1) > 0:
        print(line1)
    if len(line2) > 0:
        print(line2)
    print(city + ", " + state + " " + zip1 + " " + zip2)

if __name__ == '__main__':
    addr_name = "Иван Иванов"
    addr_line1 = "Улица"
    addr_line2 = "Площадь"
    addr_city = "СПб"    
    addr_zip = "32407"    
    print_address(addr_name, addr_line1, addr_line2, addr_city, addr_state, addr_zip)
    # добавили индекс
    addr_zip2 = "678900"
    # обновленная версия функции:
    print_address2(addr_name, addr_line1, addr_line2, addr_city, addr_state, addr_zip, addr_zip2)

