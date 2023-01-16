""" Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных. """

first_str = 'разработка'
second_str = 'сокет'
third_str = 'декоратор'

user_lst = [first_str, second_str, third_str]
print(user_lst)
for i in user_lst:
    print(f'{i} {type(i)}')

first_unicode_str = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
second_unicode_str = '\u0441\u043e\u043a\u0435\u0442'
third_unicode_str = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

user_unicode_lst = [first_unicode_str, second_unicode_str, third_unicode_str]
print(user_unicode_lst)
for i in user_unicode_lst:
    print(f'{i} {type(i)}')
    
print(first_str is first_unicode_str)