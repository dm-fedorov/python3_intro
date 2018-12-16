# dict_cinema.py
from pprint import pprint

dict_cinema = {
    'Пятница': {'time_price': {12: 250, 16: 350, 20: 450}, 'genre': 'комедия', 'limit': 16},
    'Чемпионы': {'time_price': {10: 250, 13: 350, 16: 350}, 'genre': 'спорт', 'limit': 16},
    'Пернатая банда': {'time_price': {10: 350, 14: 450, 18: 450}, 'genre': 'мультфильм', 'limit': 6}    
    }

pprint(dict_cinema)

