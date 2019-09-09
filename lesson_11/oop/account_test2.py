# Эта программа демонстрирует класс BankAccount
# с добавленным в него методом __str__.

import bankaccount2

def main():
    # Получить начальный остаток.
    start_bal = float(input('Введите свой начальный остаток: '))

    # Создать объект BankAccount.
    savings = bankaccount2.BankAccount(start_bal)

    # Внести на счет зарплату пользователя.
    pay = float(input('Сколько Вы получили на этой неделе? '))
    print('Вношу эту сумму на Ваш счет.')
    savings.deposit(pay)

    # Показать остаток.
    print(savings)

    # Получить сумму для снятия с банковского счета.
    cash = float(input('Какую сумму Вы желаете снять со счета? '))
    print('Снимаю эту сумму с Вашего банковского счета.')
    savings.withdraw(cash)

    # Показать остаток.
    print(savings)

# Вызвать главную функцию.
main()