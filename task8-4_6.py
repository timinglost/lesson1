class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Warehouse:
    def __init__(self, n):
        self.name_corporation = n
        self.all_device = []
    def AddDevice(self, device):
        self.device = device.info
        some_name = self.device['Название']
        while True:
            self.user_number = input(f'Введите количество {some_name} ')
            try:
                if not self.user_number.isdigit():
                    raise MyError('Не вводите строки, Вводите числа!')
            except MyError as d:
                print(d)
            else:
                i = 0
                while i < int(self.user_number):
                    self.device['Подразделение'] = str(input(f'В какое подразделение определить {some_name}? '))
                    self.all_device.append(self.device)
                    i += 1
                break
    @property
    def Show(self):
        for x in self.all_device:
            print(x)
        print('Количество техники ', len(self.all_device))

class OfficeEquipment:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
class Printer(OfficeEquipment):
    def __init__(self, type, name, color, price):
        super().__init__(name, color, price)
        self.type = type
        self.info = {'Тип': self.type,
                     'Название': self.name,
                     'Цвет': self.color,
                     'Цена': self.price,
                     'Подразделение': ''}
class Scanner(OfficeEquipment):
    def __init__(self, speed, name, color, price):
        super().__init__(name, color, price)
        self.speed = speed
        self.info = {'Скорость': self.speed,
                     'Название': self.name,
                     'Цвет': self.color,
                     'Цена': self.price,
                     'Подразделение': ''}
class Copier(OfficeEquipment):
    def __init__(self, uniqueness, name, color, price):
        super().__init__(name, color, price)
        self.uniqueness = uniqueness
        self.info = {'Уникальность': self.uniqueness,
                     'Название': self.name,
                     'Цвет': self.color,
                     'Цена': self.price,
                     'Подразделение': ''}
a = Scanner(233, 'LG-320', 'green', 9999.99)
b = Copier('Не уникально', 'Summsung PH-600', 'Blue', 12000)
c = Printer('Цветной', 'HP PH-001', 'Rad', 7500)
my_corp = Warehouse('Apple')
my_corp.AddDevice(a)
my_corp.AddDevice(b)
my_corp.AddDevice(c)
my_corp.Show