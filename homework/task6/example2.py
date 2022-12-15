""" Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти, оптимизировать, вновь выполнить замеры
 и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться
Описания нужно делать в виде docstrings
Более подробная информация - см. вебинар 6 """

from memory_profiler import profile

user_num = input('Введите первое число: ')
user_num1 = int(input('Введите первое число: '))
@profile()
def get_summ_isdegit(user_num):
    sum_dig = 0    
    for a in user_num:
        if a.isdigit():
            sum_dig += int(a)
    return sum_dig
get_summ_isdegit(user_num)

@profile()
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
sum_of_digits(user_num1)

@profile()
def get_summ_dig2(user_num2):
    if user_num2 < 0:
        user_num2 *= -1
    if user_num2 < 1:
        decimal_places = len(str(user_num1))
        user_num2 *= 10 ** (decimal_places-2)    
    user_num2 = int(user_num2)
    result = sum(map(int, list(str(user_num2))))
    return result
get_summ_dig2(user_num1)

""" Все тесты замеров памяти показали одинаковые результаты. 
В выбранных алгоритмах нет запросов на выделение дополнительной памяти """

