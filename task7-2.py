from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, v, h):
        self._V = v
        self._H = h
    @abstractmethod
    def area(self):
        pass

    @property
    def full_area(self):
        self.a = round((self._V / 6.5 + 0.5) + (2 * self._H + 0.3))
        return self.a

class Coat(Clothes):
    @property
    def area(self):
        return round(self._V / 6.5 +0.5)
class Costume(Clothes):
    @property
    def area(self):
        return round(2 * self._H + 0.3)


a = Coat(100, 20)
print(a.area)
print(a.full_area)



b = Costume(170, 80)
print(b.area)
print(b.full_area)
