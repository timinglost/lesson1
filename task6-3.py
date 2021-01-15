class Worker:
    def __init__(self, n, sn, p, w, b):
        self.name = n
        self.surname = sn
        self.position = p
        self._income = {'wage': w, 'bonus': b}
class Position(Worker):
    def get_full_name(self):
        print(self.name + ' ' + self.surname)
    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])
a = Position('Иван', 'Петрович', 'Програмист', 9000, 1000)
b = Position('Name', 'Surname', 'Position', 12300, 12333)
a.get_full_name()
a.get_total_income()
b.get_full_name()
b.get_total_income()
