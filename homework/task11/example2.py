""" Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных. """

first_str = 'class'
second_str = 'function'
third_str = 'method'

# вариант с преобразованием bytes

user_lst = [bytes(first_str, encoding = 'utf-8'), bytes(second_str, encoding = 'utf-8'), bytes(third_str, encoding = 'utf-8')]
for i in user_lst:
    print(f'{i} {type(i)} длинна {len(i)}')

print('\n')
first_bytes_str = b'class'
second_bytes_str = b'function'
third_bytes_str = b'method'
user_bytes_lst = [first_bytes_str, second_bytes_str, third_bytes_str]
for i in user_bytes_lst:
    print(f'{i} {type(i)} длинна {len(i)}')