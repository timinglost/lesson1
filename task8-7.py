class ComplexDigit:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return f'Комплексное сложение = {self.a + other.a} + {self.b + other.b}*i'
    def __mul__(self, other):
        return f'Комплексное умнажение = {(self.a * other.a) - (self.b * other.b)} + {(self.a * other.b) + (other.a * self.b)}*i'
x = ComplexDigit(10, 3)
y = ComplexDigit(8, 7)
print(x + y)
print(x * y)