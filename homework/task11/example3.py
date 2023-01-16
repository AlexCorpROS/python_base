""" Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode). """

first_str = 'attribute'
second_str = 'класс'
third_str = 'функция'
fourth_str = 'type'

user_lst = [first_str, second_str, third_str, fourth_str]
for i in user_lst:    
    try:
        print(i,type(i),i.encode('ascii'), 'Может быть записан в байтовом виде с помошью маркировки b')
    except:
        print(i, type(i),'Не может быть преобразован в байтовый формат без encode decode ')
