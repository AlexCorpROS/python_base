""" Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
 на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число. """

import random
user_num = int(input('Введите количесвто элементов списка: '))
user_list = []
for i in range(user_num):
    user_list.append(random.randint(-user_num,user_num))
print(f'Полученный список имеет вид: {user_list}')

# задаем значения строк в файле file.txt и считываем их в список indexs
with open('file.txt', 'w') as data:
    for i in range(user_num):
        data.write(f"{random.randrange(0, user_num)}\n")

with open('file.txt', 'r') as data:
    indexs = list(map(int,data.readlines()))
print(f'Полученные индексы {indexs}')

# Перемножаем между собой элементы user_list определенные в последовательности indexs
composition = 1
for i in range(user_num):
    composition *= user_list[indexs[i]]
print(f'Произведение элементов на указанных позициях равно {composition}')
