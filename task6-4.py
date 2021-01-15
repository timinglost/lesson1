import random
class Car:
    def __init__(self, s, c, n, i):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = i
    def go(self):
        print(f'Машина {self.name} поехала.')
    def stop(self):
        print(f'Машина {self.name} остановилась.')
    def turn(self, direction):
        a = random.choice(['лево', 'право'])
        print(f'Машина {self.name} повернула на {a}.')
        # ИЛИ
        print(f'Машина {self.name} повернула на {direction}.')
    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч.')
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Вы превысили скорость!')
        else:
            print(f'Текущая скорость {self.speed} км/ч.')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили скорость!')
        else:
            print(f'Текущая скорость {self.speed} км/ч.')
class PoliceCar(Car):
    pass

a = Car(100, 'Green', 'BMW', True)
a.turn(str(input('Введите куда повернуть ')))
a.show_speed()
a.go()
a.stop()
print(a.speed)
print(a.color)
print(a.name)
print(a.is_police)

b = TownCar(10, 'Green', 'BMW', True)
b.turn(str(input('Введите куда повернуть ')))
b.show_speed()
b.go()
b.stop()
print(b.speed)
print(b.color)
print(b.name)
print(b.is_police)

c = WorkCar(1000, 'Green', 'BMW', False)
c.turn(str(input('Введите куда повернуть ')))
c.show_speed()
c.go()
c.stop()
print(c.speed)
print(c.color)
print(c.name)
print(c.is_police)

d = PoliceCar(10003, 'Green', 'BMW3', False)
d.turn(str(input('Введите куда повернуть ')))
d.show_speed()
d.go()
d.stop()
print(d.speed)
print(d.color)
print(d.name)
print(d.is_police)
