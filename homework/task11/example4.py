""" Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode). """

first_str = 'разработка'
second_str = 'администрирование'
third_str = 'protocol'
fourth_str = 'standard'
user_lst = [first_str, second_str, third_str, fourth_str]
for i in user_lst:
    i = i.encode('utf-8')
    print(f'{i} {type(i)}')
    i = i.decode('utf-8')
    print(f'{i} {type(i)} \n')
