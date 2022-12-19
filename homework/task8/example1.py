""" Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:                 Сумма матриц:   
1 2 3       1 2 3       2  4  6
4 5 6       4 5 6       8  10 12
7 8 9       7 8 9       14 16 18
"""

import numpy
from random import randint

""" a = numpy.zeros((3, 3))
lowerBound = int(input("Введите нижнюю границу. "))
upperBound = int(input("Введите верхнюю границу. "))
for i in range(3):
    for j in range(3):
        a[i][j] = randint(lowerBound, upperBound)      
print(type(a)) """



class Matrix():

    def __init__(self, lst):
        self.lst = lst
        self.row_count = len(self.lst)
        self.col_count = len(self.lst[0])

    def __str__(self):
        ret_val = ''
        for i in range(self.row_count):
            for j in range(self.col_count):
                ret_val +=  str(self.lst[i][j]) + '\t'
            ret_val += '\n'

        return ret_val

    def get_item(self, row, col):
        try:
            ret_val = self.lst[row][col]
        except:
            ret_val = 0

        return ret_val

    def __add__(self, other):

        new_lst = []
        max_rows = max(self.row_count, other.row_count)
        max_cols = max(self.col_count, other.col_count)

        for i in range(max_rows):
            new_lst.append([])
            for j in range(max_cols):
                new_lst[i].append(self.get_item(i, j) + other.get_item(i, j))

        return Matrix(new_lst)


m1 = Matrix(create_lst())
print(m1)

m2 = Matrix(create_lst())
print(m2)

m3 = m1 + m2
print(m3)
