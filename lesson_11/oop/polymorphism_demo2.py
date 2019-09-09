# Эта программа демонстрирует полиморфизм.

import animals

def main():
    # Создать объект Mammal, объект Dog и
    # объект Cat.
    mammal = animals.Mammal('обычное животное')
    dog = animals.Dog()
    cat = animals.Cat()

    # Показать информацию о каждом животном.
    print('Вот несколько животных и')
    print('звуки, которые они издают.')
    print('--------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    print()
    show_mammal_info('Я – цепочка символов')

# Функция show_mammal_info принимает объект
# в качестве аргумента и вызывает свои методы 
# show_species и make_sound.

def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('Это не млекопитающее животное!')

# Вызвать главную функцию.
main()