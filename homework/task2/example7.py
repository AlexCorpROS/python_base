""" Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11 """

# Решение через метод isdigit()

sum_dig = 0
user_num = input('Введите первое число: ')
for a in user_num:
    if a.isdigit():
        sum_dig += int(a)
print(f'Сумма цифр числа {user_num} равна {sum_dig}')

# Решения математическим методом

user_num1 = float(input('Введите второе число : '))
if user_num1 < 0:
    user_num1 *= -1
if user_num1 < 1:
    decimal_places = len(str(user_num1))
    user_num1 *= 10 ** (decimal_places-2)    
user_num1 = int(user_num1)

def sum_of_digits(num):
    sum1 = 0
    while num > 0:
        sum1 += num % 10
        num //= 10
    return sum1
print(f'Сумма цифр числа {user_num1} равна {sum_of_digits(user_num1)}')

# Решение через sum и map
print(f'Сумма цифр числа {user_num1} равна {sum(map(int, list(str(user_num1))))}. Второй вывод')
