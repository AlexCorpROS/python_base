# 1) Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
# и строк и сохраните в переменные, выведите на экран.

a = 12
b = 1.2
c = 'privet'
d = True
print(f'int {a}, float {b}, str {c} and boolean {d}')
print(type(a),type(b),type(c),type(d))

# Ввод данных  с клавиатуры

list = []
user_list = input('Введите строки через пробел :').split()
print(user_list)
print(type(user_list))
user_num_list = user_list
print(user_num_list)
print(type(user_num_list))