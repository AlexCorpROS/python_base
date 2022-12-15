""" Для теста выбраны различные решения седьмого задания второго семинара """
# Решение через метод isdigit()

def get_summ_isdegit(user_num):
    sum_dig = 0    
    for a in user_num:
        if a.isdigit():
            sum_dig += int(a)
    return sum_dig

# Решения математическим методом

def sum_of_digits(user_num1):
    if user_num1 < 0:
        user_num1 *= -1
    if user_num1 < 1:
        decimal_places = len(str(user_num1))
        user_num1 *= 10 ** (decimal_places-2)    
    user_num1 = int(user_num1)

    sum1 = 0
    while user_num1 > 0:
        sum1 += user_num1 % 10
        user_num1 //= 10
    return sum1

# Решение через sum и map

def get_summ_dig2(user_num2):
    if user_num2 < 0:
        user_num2 *= -1
    if user_num2 < 1:
        decimal_places = len(str(user_num1))
        user_num2 *= 10 ** (decimal_places-2)    
    user_num2 = int(user_num2)
    result = sum(map(int, list(str(user_num2))))
    return result

user_num = input('Введите первое число: ')
print(f'Сумма цифр числа {user_num} равна {get_summ_isdegit(user_num)}')
user_num1 = float(input('Введите второе число : '))
print(f'Сумма цифр числа {user_num1} равна {sum_of_digits(user_num1)}')
user_num2 = float(input('Введите третье число : '))
print(f'Сумма цифр числа {user_num2} равна {get_summ_dig2(user_num2)}.')