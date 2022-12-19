"""  Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
 is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
 остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
 Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
 Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
  и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
 Выполните вызов методов и также покажите результат. """

class Car:

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return print(f'Машина {self.name} поехала.')

    def stop(self):
        return print(f'Машина {self.name} остановилась.')

    def turn(self, direction):
        return print(f'Машина {self.name} повернула на {direction}')

    def show_speed(self):
        return print(f'Текущая скорость {self.speed}')

class TownCar(Car):

    def show_speed(self):
              
        if self.speed > 60:
            return print(f'Скорость превышает разрешенные 60 км/ч. Твоя скорость {self.speed}')
        else:
            return print(f'Твоя скорость {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print(f'Скорость превышает разрешенные 40 км/ч. Твоя скорость {self.speed}')
        else:
            return print(f'Твоя скорость {self.speed}')

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

car_1 = SportCar('ВАЗ', 70, 'Серый', False)
print(car_1.name)
car_1.name = 'Веста'
print(f'Название изменено на {car_1.name}')

car_2 = TownCar('ГАЗ', 80, 'Красный', False)
car_2.show_speed()
car_2.speed = 60
car_2.show_speed()

car_3 = PoliceCar('УАЗ', 90 ,'Синий', True)
car_3.go()
car_3.turn('Советская')
car_3.stop()