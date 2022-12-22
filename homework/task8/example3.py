""" Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой. """

class Div_Null(Exception):
    def div_null(divisible, divider):
        try:
            return (divisible / divider)
        except:
            return ('Деление на ноль недопустимо. И точка')

user_num1 = float(input('Введите делимое: '))
user_num2 = float(input('Введите делитель: '))
print(Div_Null.div_null(user_num1, user_num2))
