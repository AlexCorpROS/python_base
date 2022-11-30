""" Реализуйте алгоритм перемешивания списка. """

import random
user_num = int(input('Введите количесвто элементов списка: '))
user_list = []
for i in range(user_num):
    user_list.append(random.randint(-user_num,user_num))
print(f'Полученный список имеет вид: {user_list}')
random.shuffle(user_list)
print(f"Cписок после первого перемешивания:{user_list}")
random.shuffle(user_list)
print(f"Cписок после второго перемешивания:{user_list}")