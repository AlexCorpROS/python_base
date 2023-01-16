# Функции и классы для тестов

# Нахождение суммы двух наибольших чисел

def my_sum_maxvalue(arg1, arg2, arg3):
    result = arg1 + arg2 + arg3 - min([arg1, arg2, arg3])
    print(f'Сумма двух наибольших значений равна: {result}')
    return result

# Возведение в степень

def my_func_exponent(x, y):
    result = x**y
    print(f'Число {x} в степени {y} равно {result}')
    return result

# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

def my_func_moreprev(user_lst):
    return [user_lst[i] for i in range(1, len(user_lst)) if user_lst[i] > user_lst[i - 1]]

# Копирование объекта

def get_copy(a):
    result = a
    return result

# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.

class Road:
    _weight = 25     # вес 1м2 полотна толщиной 1 см
    _height = 5      # толщина полотна
    def __init__(self, length, width):
        self._length = length
        self._width = width        

    def calculation_mass(self):
        asphalt_mass = self._length * self._width * self._weight * self._height / 1000
        result = round(asphalt_mass)
        print(f'Для покрытия участка дорожного полотна неободимо {result} тонн(ы) асфальта')
        return result


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль

class Div_Null(Exception):
    def __init__(self, txt):
        self.txt = txt

def div_null(divisible, divider):           
    if divider == 0:
         raise Div_Null(f'На ноль делить нельзя. И точка')
    else:
        return divisible / divider

