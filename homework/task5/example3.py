""" Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32 """

with open(r"homework\task5\testex3.txt", 'r', encoding='utf-8') as text:
    f_text = text.readlines()
    total_income = 0
    list = [] 
    for line in f_text:
        family, income = line.split()
        income = float(income)
        total_income += income
        if income < 20000:
            list.append(family)
    print(f'Средий доход сотрудников равен {total_income / len(f_text):.2f}')
    print(f'Список сотрудников с доходом ниже 20000 {list}')      

