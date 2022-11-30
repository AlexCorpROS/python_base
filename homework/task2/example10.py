""" Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
 на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число. """

from random import randint
user_num = int(input('Введите количесвто элементов списка: '))
user_list = []
for i in range(user_num):
    user_list.append(randint(-user_num,user_num))
print(f'Полученный список имеет вид: {user_list}')

x = open('file.txt','r')
print(x)
""" result = user_list[int(x.readline())] * numbers[int(x.readline(2))]
print(result) """
