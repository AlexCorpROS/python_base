""" Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 """

x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))

if x > 0 and y > 0:
    print(f'Координаты точки {x,y} ннаходятся в первой четверти(правая верхняя)')
elif x < 0 and y > 0:
    print(f'Координаты точки {x,y} ннаходятся во второй четверти(левая верхняя)')
elif x < 0 and y < 0:
    print(f'Координаты точки {x,y} ннаходятся в третьей четверти(левая нижняя)')
elif x > 0 and y < 0:
    print(f'Координаты точки {x,y} ннаходятся в четвертой четверти(правая нижняя)')
elif x == 0 and y != 0:
    print(f'Точка {x,y} находится на оси абсцисс(x)')
elif x!= 0 and y== 0:
    print(f'Точка {x,y} находится на оси ординат(y)')
else:
    print('Координаты нулевые, точка находится в центре отсчета')
