""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
    Перевод на русский > не (X или Y или Z) = не X "логический И" не Y "логический И" не Z    
"""

x = input('Введите значение X: ')
y = input('Введите значение Y: ')
z = input('Введите значение Z: ')
left = not(x or y or z)
right = not(x) and not(y) and not(z)
if left == right:
    print(f'Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z верно для значения X={x}, Y={y}, Z={z}')
else:
    print(f'Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z не верно для значения X={x}, Y={y}, Z={z}')