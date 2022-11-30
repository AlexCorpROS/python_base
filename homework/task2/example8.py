""" Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

user_num = int(input('Введите натуральное число: '))
user_list = []
temp = 1
for i in range(user_num): 
    i = i + 1   
    temp = temp * i  
    user_list.append(temp)
print(user_list)
