from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, v, h):
        self._V = v
        self._H = h
    @abstractmethod
    def area(self):
        pass
    def full_area(self):
        self.a = (self._V / 6.5 + 0.5) + (2 * self._H + 0.3)
        return self.a
    @property
    def error(self):
        try:
            if self._V < 0 or self._H < 0:
                print('Введены некоректные данные')
            return self._V, self._H
        except TypeError:
            print('Введите число')
class Coat(Clothes):
    def area(self):
        return self._V / 6.5 +0.5
class Costume(Clothes):
    def area(self):
        return 2 * self._H + 0.3


a = Coat(100, 20)
print(a.area())
print(a.full_area())
a.error


b = Costume(170, 80)
print(b.area())
print(b.full_area())

c = Coat(23, 'ff')
c.error