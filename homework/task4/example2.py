""" Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше
предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать
генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]. """

from random import randint

user_list = [randint(0, 100) for i in range(20)]
print(f'Исходный список: {user_list}')
processed_list = []
for i in range(1,len(user_list)-1):
    if user_list[i] > user_list[i-1]:
        processed_list.append(user_list[i])
print(processed_list)
