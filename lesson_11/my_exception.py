# my_exception.py

# Определяем собственное исключение:
class MyError(Exception):
    pass

try:
    raise MyError("Что-то пошло не так...")
except MyError as error:
    print("Поймали исключение:", error)

