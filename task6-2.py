class Road:
    def __init__(self, l, w):
        self._lenght = l
        self._width = w
    # Масса = Плотность * объем, плотность асфальта взята из интернета
    def mass(self):
        self.thickness = int(input('Введите толщену асфальта в см ')) / 100
        self.density_of_asphalt = 1300
        self.volume = self._lenght * self._width * self.thickness
        return self.volume * self.density_of_asphalt
a = Road(int(input('Введите длину в метрах ')), int(input('Введите ширину в метрах ')))
print(a.mass())