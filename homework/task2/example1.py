""" Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать
у пользователя, а указать явно, в программе. """

test_list = [1, 1.2, "toronto" None , True]
for i in test_list:
    print(type(test_list[i]))