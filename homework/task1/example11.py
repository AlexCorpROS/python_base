""" Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между
 ними в 2D пространстве.

Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21 """
point_one = input('Введите координаты первой точки через пробел: ').split()
point_two = input('Введите координаты второй точки через пробел: ').split()
decimal_places = int(input('Сколько заков после запятой выводить на печать: '))
point_sign = 10 ** decimal_places
coordinate1 = list(map(float,point_one))
coordinate2 = list(map(float,point_two))
distance = ((coordinate2[0] - coordinate1[0]) ** 2 + (coordinate2[1] - coordinate1[1]) ** 2) ** (0.5)
x = distance*point_sign//1/point_sign
print(f'Расстояние между точками {point_one} {point_two} равно {x}')

# Решение с простым округлением имеет вид 
# print(f'Расстояние между точками {point_one} {point_two} равно {distance:.2f}')
# но дает результат отличный от примера в условии задачи