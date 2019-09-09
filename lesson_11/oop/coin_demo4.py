# Эта программа импортирует модуль coin и
# создает экземпляр класса Coin.

import coin

def main():
    # Создать объект на основе класса Coin.
    my_coin = coin.Coin()

    # Показать обращенную вверх сторону монеты.
    print('Эта сторона обращена вверх:', my_coin.get_sideup())

    # Подбросить монету.
    print('Собираюсь подбросить монету десять раз:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Вызвать главную функцию.
main()