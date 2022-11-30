""" Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
 относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict. """

month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Мая', 'Июнь', 'Июль', 'Август', 'Сентябрь',
'Октябрь', 'Ноябрь', 'Декабрь']
season_list = ['зима', 'весна', 'лето', 'осень']

user_num = int(input('Введите номер месяца: '))
if user_num == 12 or user_num == 1 or user_num == 2:
    print(f'{month_list[user_num-1]} это {season_list[0]}')
elif user_num == 3 or user_num == 4 or user_num == 5:
    print(f'{month_list[user_num-1]} это {season_list[1]}')
elif user_num == 6 or user_num == 7 or user_num == 8:
    print(f'{month_list[user_num-1]} это {season_list[2]}')
elif user_num == 9 or user_num == 10 or user_num == 11:
    print(f'{month_list[user_num-1]} это {season_list[3]}')
else:
    print(f'В принятом году всего 12 месяцев, вы ввели {user_num}')

month_dict = {1 : 'Январь', 2 : 'Февраль', 3: 'Март', 4 : 'Апрель', 5: 'Мая', 6: 'Июнь', 7 : 'Июль', 8 : 'Август',
 9 : 'Сентябрь', 10 : 'Октябрь', 11 : 'Ноябрь', 12 : 'Декабрь'}
season_dict = {1 :'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}

user_num2 = int(input('Введите еще один номер месяца: '))
if user_num2 == 12 or user_num2 == 1 or user_num2 == 2:
    print(f'{month_dict.get(user_num2)} это {season_dict.get(1)}')
elif user_num2 == 3 or user_num2 == 4 or user_num2 == 5:
    print(f'{month_dict.get(user_num2)} это {season_dict.get(2)}')
elif user_num2 == 6 or user_num2 == 7 or user_num2 == 8:
    print(f'{month_dict.get(user_num2)} это {season_dict.get(3)}')
elif user_num2 == 9 or user_num2 == 10 or user_num2 == 11:
    print(f'{month_dict.get(user_num2)} это {season_dict.get(4)}')
else:
    print(f'В принятом году всего 12 месяцев, вы ввели {user_num2}')