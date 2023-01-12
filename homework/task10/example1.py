""" Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ
Создать метакласс для паттерна Синглтон """

class CorrectType:
    def __set__(self, instance, value):
        if type(value) not in (int, float):
            raise TypeError(f'{self.my_attr} должен быть числом')   
        elif value < 0:
            raise ValueError(f'Значение не может быть отрицательным')     
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class NonNegativ:
    def __set__(self, instance, value):
        if type(value) not in (int, float):
            raise TypeError(f'Параметр {self.my_attr} должен быть числом')
        elif value < 0:
            raise ValueError(f'Значение {self.my_attr} не должно быть отрицательным')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class СheckInput:
    def __set__(self, instance, value):
        if type(value) != str:
            raise TypeError(f'Параметр {self.my_attr} должен быть строкой')        
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class Road:
    length = CorrectType()
    width = CorrectType()

    _weight = 25     # вес 1м2 полотна толщиной 1 см
    _height = 5      # толщина полотна

    def __init__(self, length, width):
        self.length = length
        self.width = width        

    def calculation_mass(self):
        asphalt_mass = self.length * self.width * self._weight * self._height / 1000
        print(f'Для покрытия участка дорожного полотна неободимо {round(asphalt_mass)} тонн(ы) асфальта')


class Worker():
    name = СheckInput()
    surname = СheckInput()
    wage = NonNegativ()
    bonus = NonNegativ()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):
   
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self.wage + self.bonus

    def __str__(self):
        return f"Name: {self.get_full_name()}  Salary: {self.get_total_income()}"

f = Road( 10, 1000)
f.calculation_mass()

dor = Position('авbkljd', 'Sdf', 2 , 2 ,21)
print(dor)