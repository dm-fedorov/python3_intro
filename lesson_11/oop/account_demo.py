# Эта программа создает экземпляр класса SavingsAccount
# и экземпляр класса CD.

import accounts

def main():
    # Получить номер счета, процентную ставку,
    # и остаток сберегательного счета.
    print('Введите данные о сберегательном счете.')
    acct_num = input('Номер счета: ')
    int_rate = float(input('Процентная ставка: '))
    balance = float(input('Остаток: '))

    # Создать объект SavingsAccount.
    savings = accounts.SavingsAccount(acct_num, int_rate,
                                      balance)

    # Получить номер счета, процентную ставку,
    # остаток счета и дату погашения счета CD.
    print('Введите данные о счете CD.')
    acct_num = input('Номер счета: ')
    int_rate = float(input('Процентная ставка: '))
    balance = float(input('Остаток: '))
    maturity = input('Дата погашения: ')

    # Создать объект CD.
    cd = accounts.CD(acct_num, int_rate, balance, maturity)

    # Показать введенные данные.
    print('Вот введенные Вами данные:')
    print()
    print('Сберегательный счет')
    print('-------------------')
    print('Номер счета:', savings.get_account_num())
    print('Процентная ставка:', savings.get_interest_rate())
    print('Остаток: $',
          format(savings.get_balance(), ',.2f'),
          sep='')
    print()
    print('Счет депозитного сертификата (CD)')
    print('---------------------------------')
    print('Номер счета:', cd.get_account_num())
    print('Процентная ставка:', cd.get_interest_rate())
    print('Остаток: $',
          format(cd.get_balance(), ',.2f'),
          sep='')
    print('Дата погашения:', cd.get_maturity_date())

# Вызвать главную функцию.
main()