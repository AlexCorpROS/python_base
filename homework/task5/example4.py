""" Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
текстовый файл. """

rus_dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
format_text = []   
with open(r"homework\task5\testex4.txt", 'r+' , encoding='utf-8') as text:
    f_text = text.readlines()
    print(f'Исходная запись {f_text}')      
    for line in f_text:
        line = line.split(' ', 1)
        format_text.append(rus_dict[line[0]] + ' ' + line[1])
    print(f'Запись с заменой {format_text}')

with open(r"homework\task5\testex4_rus.txt", 'w', encoding='utf-8') as text_rus:
    text_rus.writelines(format_text)