""" Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени, оптимизировать, вновь выполнить замеры
и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться """

from timeit import timeit
from user_scripts import get_summ_isdegit, sum_of_digits, get_summ_dig2

test1 = timeit("get_summ_isdegit", globals=globals())
test2 = timeit("sum_of_digits", globals=globals())
test3 = timeit("get_summ_dig2", globals=globals())
print(f'Значение скорости выполнения скрипта\n get_summ_isdegit {test1}\n sum_of_digits {test2}\n'
    f' get_summ_dig2 {test3}\nМинимальная время исполнения скрипта {min(test1, test2, test3)}')

t_min = min(test1, test2, test3)
if t_min == test1:
    print('Минимальное время выполнения у скрипта get_summ_isdegit')
elif t_min == test2:
    print('Минимальное время выполнения у скрипта sum_of_digits')
else:
    print('Минимальное время выполнения у скрипта get_summ_dig2')

""" По итогам замера сторости исполнения скриптов в типовой задаче самым эффективным оказался метод использующий
встроеннst функцию sum и map. Вторым по производительности оказался пользовательский скрипт математического метода.
И самым медленным метод isdigit, однако при малой длине числа это метод работает быстрее математического,
 но все равно уступает встроенной функции sum """

    