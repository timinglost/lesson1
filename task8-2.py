class Del(Exception):
    def __init__(self, txt):
        self.txt = txt

a = float(input('Введите делимое '))
b = float(input('Введите делитель '))
try:
    if b == 0:
        raise Del('Деление на ноль!')
except Del as d:
    print(d)
else:
    print(a / b)