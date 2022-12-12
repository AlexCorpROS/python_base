""" Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка. """

work_file = open('test5ex1.txt', 'w')
user_text = input('Введите текст. Пустая строка заканчивает ввод: ')
while user_text:
    work_file.write(user_text + '\n') # запись в файл построчно
    user_text = input('Введите текст \n')
    if not user_text:
        break
work_file.close()

with open(r"test5ex1.txt") as text:    
    f_text = text.readlines() # вывод списком
    print(f_text)
    for line in text: # вывод построчно
        print(line)
