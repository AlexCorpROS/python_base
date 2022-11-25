"""  1) Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
 и строк и сохраните в переменные, выведите на экран. """

a = 12
b = 1.2
c = 'privet'
d = True
print(f'int {a}, float {b}, str {c} and boolean {d}')
print(type(a),type(b),type(c),type(d))

# Ввод данных  с клавиатуры c типом str

user_list = input('Введите значения через пробел :')
print(print(f'Список введенных значенний имеет вид {user_list} и тип хранимых дданных {type(user_list[0])}'))

# Ввод данных  с клавиатуры c преобразованием в тип int через цикл while

user_num = (input('Введите цифровые значения через пробел: ')).split()
i = 0
user_numlist = [i for i in range(len(user_num))] 
while i < len(user_num):
    user_numlist[i] = int(user_num[i])
    i+=1
print(f'Список введенных значенний имеет вид {user_numlist} и тип хранимых дданных {type(user_numlist[0])}')

# Ввод данных  с клавиатуры c преобразованием в тип int используя функцию map

user_num = (input('Введите второе цифровые значения через пробел: ')).split()
user_numlist2 = list(map(int,user_num))
print(f'Список введенных значенний имеет вид {user_numlist2} и тип хранимых данных {type(user_numlist2[0])}')
