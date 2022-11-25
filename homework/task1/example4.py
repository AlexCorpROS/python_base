""" Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции. """

user_num = int(input('Введите целое положительное число :'))
max_num = 0
work_num = [user_num][0]
while work_num  > 0:
    temp_num = work_num  % 10
    if temp_num > max_num:
        max_num = temp_num
    work_num  //=10
print(f'Самая большая цифра в числе {user_num} равна {max_num}') 
