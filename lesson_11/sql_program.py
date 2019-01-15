# sql_program.py

import sqlite3
# создание подключения к базе данных
conn = sqlite3.connect('tasks.db')
# создание курсора для подключения
cursor = conn.cursor()
# выполнение запроса с курсором (запускается один раз для создания таблицы)
cursor.execute("create table tasks (id integer prime key, category text, name text, time text)")

# добавление строки в таблицу (по мере необходимости)
cursor.execute("insert into tasks (id, category, name, time) values (NULL, ?, ?, ?)", 
                    ('Поход в магазин', 'Купить сливочное масло', '12:12:13' ))

# закрепление транзакции к базе данных:
conn.commit()

# запрашиваем все строки таблицы tasks
result = cursor.execute('select * from tasks') 

# возвращение результатов запроса;
print(result.fetchall())

# закрытие подключения
conn.close()
