# Эта программа чертит круговую диаграмму на элементе Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        self.__CANVAS_WIDTH = 320    # Ширина холста
        self.__CANVAS_HEIGHT = 240   # Высота холста
        self.__X1 = 60     # Левая верхняя координата X ограничивающего прямоугольника 
        self.__Y1 = 20     # Левая верхняя координата Y ограничивающего прямоугольника
        self.__X2 = 260    # Нижняя правая координата X ограничивающего прямоугольника
        self.__Y2 = 220    # Нижняя правая координата Y ограничивающего прямоугольника
        self.__PIE1_START = 0     # Исходный угол сектора 1
        self.__PIE1_WIDTH = 45    # Протяженность сектора 1
        self.__PIE2_START = 45    # Исходный угол сектора 2
        self.__PIE2_WIDTH = 90    # Протяженность сектора 2
        self.__PIE3_START = 135   # Исходный угол сектора 3
        self.__PIE3_WIDTH = 120   # Протяженность сектора 3
        self.__PIE4_START = 255   # Исходный угол сектора 4
        self.__PIE4_WIDTH = 105   # Протяженность сектора 4
 
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Canvas.
        self.canvas = tkinter.Canvas(self.main_window,
                                     width=self.__CANVAS_WIDTH,
                                     height=self.__CANVAS_HEIGHT)

        # Начертить сектор 1.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, 
                               self.__Y2, start=self.__PIE1_START,
                               extent=self.__PIE1_WIDTH,
                               fill='red')

        # Начертить сектор 2.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, 
                               self.__Y2, start=self.__PIE2_START,
                               extent=self.__PIE2_WIDTH,
                               fill='green')

        # Начертить сектор 3.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, 
                               self.__Y2, start=self.__PIE3_START,
                               extent=self.__PIE3_WIDTH,
                               fill='black')

        # Начертить сектор 4.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, 
                               self.__Y2, start=self.__PIE4_START,
                               extent=self.__PIE4_WIDTH,
                               fill='yellow')
 
        # Упаковать холст.
        self.canvas.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()