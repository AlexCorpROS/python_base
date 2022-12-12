""" Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке. """

with open(r"homework\task5\testex2.txt",  'w', encoding='utf-8') as text:
    user_text = input('Введите текст. Пустая строка заканчивает ввод: ')
    while user_text:
        text.write(user_text + '\n') 
        user_text = input('Введите текст \n')
        if not user_text:
            break    

with open(r"homework\task5\testex2.txt") as text:
    f_text = text.readlines() 
    print(f'Всего в файле {len(f_text)} строки')
    for i, j in enumerate(f_text):
                print(f"В строке {i + 1}: {len(j.split())} слов(а)")
    

