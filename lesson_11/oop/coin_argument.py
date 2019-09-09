# Эта программа передает объект Coin
# в качестве аргумента в функцию.
import coin

# Главная функция
def main():
    # Создать объект Coin.
    my_coin = coin.Coin()

    # Эта инструкция покажет 'Орел'.
    print(my_coin.get_sideup())

    # Передать объект в функцию flip.
    flip(my_coin)

    # Эта инструкция может показать 'Орел' 
    # либо 'Решка'.
    print(my_coin.get_sideup())

# Функция flip подбрасывает монету.
def flip(coin_obj):
    coin_obj.toss()

# Вызвать главную функцию.
main()