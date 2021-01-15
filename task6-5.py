class Stationery:
    def __init__(self, t):
        self.title = t
    def drow(self):
        print(f'{self.title}. Запуск отрисовки.')
class Pen(Stationery):
    def drow(self):
        print(f'{self.title}. Запуск отрисовки ручкой.')
class Pencil(Stationery):
    def drow(self):
        print(f'{self.title}. Запуск отрисовки карандашом.')
class Handle(Stationery):
    def drow(self):
        print(f'{self.title}. Запуск отрисовки маркером.')

a = Stationery('One')
a.drow()

b = Pen('Tow')
b.drow()

c = Pencil('Three')
c.drow()

d = Handle('4')
d.drow()