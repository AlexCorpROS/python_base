from random import randint

class Matrix():

    def __init__(self, lst):
        self.lst = lst
        self.row = len(self.lst)
        self.col = len(self.lst[0])

    def __str__(self):
        mod_matrix = ''
        for i in range(self.row):
            for j in range(self.col):
                mod_matrix +=  str(self.lst[i][j]) + '\t'
            mod_matrix += '\n'

        return mod_matrix

    def get_item(self, row, col):
        try:
            mod_matrix = self.lst[row][col]
        except:
            mod_matrix  = 0

        return mod_matrix 

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
print(f'Второй список списков{a}')
m1 = Matrix(a)
print(f'Первая матрица \n{m1}')
m2 = Matrix(b)
print(f'Вторая матрица \n{m1}')
m3 = m1 + m2
print(f'Сумма двух матриц \n{m3}')