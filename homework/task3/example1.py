""" Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль. """

def division(divisible,divider):          
    try:
        return divisible/divider
    except ZeroDivisionError:
        print('Делить на ноль нельзя')        
print(division(float(input('Введите первое число: ')),float(input('Введите второе число: '))))

