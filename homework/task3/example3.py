""" Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
 наибольших двух аргументов. """

def my_func(arg1, arg2, arg3):
    print(f'Сумма двух наибольших значений равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')

my_func(int(input('Введите первое значение: ')),
    int(input('Введите второе значение: ')),
    int(input('Введите третье значение: ')),)