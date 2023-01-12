# Создать метакласс для паттерна Синглтон

class MySingle(type):

    base = None
   
    def __call__(cls, *args, **kwargs):
        if cls.base is None:
            cls.base = super().__call__(*args, **kwargs)
            return cls.base
        return cls.base
    
class God(metaclass = MySingle):

    def __init__(self, power):
        self.power = power

A1 = God(1)
A2 = God(5)

print(A1 is A2)
print(A2.power)
A2.power = 8
print(A2.power)

print('Пропуск')
print(A1.power)