""" Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369."""

user_number = input('Введдите число:')
user_transformation = int(user_number) + int(user_number * 2) + int(user_number * 3)
print(f'Сумма чисел по формуле n + nn + nnn для числа {user_number} равна {user_transformation} ')