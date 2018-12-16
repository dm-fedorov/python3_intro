from tkinter import *
root = Tk()
 
Label(text="Имя:").grid(row=0, column=0)
table_name = Entry(width=30)
table_name.grid(row=0, column=1, columnspan=3)
 
Label(text="Столбцов:").grid(row=1, column=0)
table_column = Spinbox(width=7, from_=1, to=50)
table_column.grid(row=1, column=1)
Label(text="Строк:").grid(row=1, column=2)
table_row = Spinbox(width=7, from_=1, to=100)
table_row.grid(row=1, column=3)
 
Button(text="Справка").grid(row=2, column=0)
Button(text="Вставить").grid(row=2, column=2)
Button(text="Отменить").grid(row=2, column=3)
 
root.mainloop()
