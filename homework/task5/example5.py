""" Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран. """

with open(r"homework\task5\testex5.txt", 'w' , encoding='utf-8') as text:
    numbers = input('Введите числа через пробел: ')
    text.writelines(numbers)
    user_num = numbers.split()
    print(sum(map(float, user_num)))