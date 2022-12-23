""" Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой. """

class Div_Null(Exception):
    def __init__(self, txt):
        self.txt = txt

def div_null():
    try:
        divisible = float(input('Введите делимое: '))
        divider = float(input('Введите делитель: '))
        if divider == 0:
            raise Div_Null(f'На ноль делить нельзя. И точка')
        else:
            return divisible / divider
    except ValueError:
        return "Вы ввели не число"
    except Div_Null as err:
        return err

print(div_null())
