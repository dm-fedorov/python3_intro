# Эта программа демонстрирует класс BankAccount.

import bankaccount

def main():
    # Получить начальный остаток.
    start_bal = float(input('Введите свой начальный остаток: '))

    # Создать объект BankAccount.
    savings = bankaccount.BankAccount(start_bal)

    # Внести на счет зарплату пользователя.
    pay = float(input('Сколько Вы получили на этой неделе? '))
    print('Вношу эту сумму на Ваш счет.')
    savings.deposit(pay)

    # Показать остаток.
    print('Ваш остаток на банковском счете составляет $',
          format(savings.get_balance(), ',.2f'),
          sep='')

    # Получить сумму для снятия с банковского счета.
    cash = float(input('Какую сумму Вы желаете снять со счета? '))
    print('Снимаю эту сумму с Вашего банковского счета.')
    savings.withdraw(cash)

    # Показать остаток.
    print('Ваш остаток на банковском счете составляет $',
          format(savings.get_balance(), ',.2f'),
          sep='')

# Вызвать главную функцию.
main()