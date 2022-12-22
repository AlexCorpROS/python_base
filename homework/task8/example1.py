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
        self.row = len(self.lst)
        self.col = len(self.lst[0])

    def __str__(self):
        convert_matrix = ''
        for i in range(self.row):
            for j in range(self.col):
                convert_matrix +=  str(self.lst[i][j]) + '\t'
            convert_matrix += '\n'

        return convert_matrix

    def get_item(self, row, col):
        try:
            convert_matrix = self.lst[row][col]
        except:
            convert_matrix = 0

        return convert_matrix

    def __add__(self, second):

        new_lst = []
        max_rows = max(self.row, second.row)
        max_cols = max(self.col, second.col)

        for i in range(max_rows):
            new_lst.append([])
            for j in range(max_cols):
                new_lst[i].append(self.get_item(i, j) + second.get_item(i, j))

        return Matrix(new_lst)

def get_matrix_1st(row, col):    
    matrix_list = []
    for i in range(row):
        matrix_list.append([])
        for j in range(col):
            matrix_list[i].append(randint(0, 99))
    return matrix_list

a = get_matrix_1st(3,3)
print(f'Первый список списков{a}')
b = get_matrix_1st(3,3)
print(f'Второй список списков{b}')
m1 = Matrix(a)
print(f'Первая матрица \n{m1}')
m2 = Matrix(b)
print(f'Вторая матрица \n{m2}')
m3 = m1 + m2
print(f'Сумма двух матриц \n{m3}')
