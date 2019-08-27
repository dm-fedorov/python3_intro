# check_ip.py
import ipaddress

# Функция check_ip проверяет является ли аргумент, который ей передали, IP-адресом. 
def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError as err:
        return False

if __name__ == "__main__":
    result = check_ip('10.1.1.1')
    print('Результат:', result)
