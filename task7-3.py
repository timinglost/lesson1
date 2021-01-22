class Cell:
    def __init__(self, c):
        self.cell = int(c)
    def __add__(self, other):
        self.cell += other
    def __sub__(self, other):
        self.cell -= other
    def __mul__(self, other):
        self.cell *= other
    def __truediv__(self, other):
        a = self.cell / other
        self.cell = int(a)
    def make_order(self, n):
        self.num = n
        i = 0
        i1 = 1
        my_str = ''
        while i < self.cell:
            my_str += '*'
            if i1 == self.num:
                my_str += '\n'
                i1 = 0
            i += 1
            i1 += 1
        print(my_str)


b = Cell(12)
b.make_order(5)





a = Cell(10)
a + 20
a - 10
a * 2
a / 2
print(a.cell)
