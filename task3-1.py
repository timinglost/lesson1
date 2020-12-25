a = float(input('Введите делимое '))
b = float(input('Введите делитель '))
def division(x, y):
    if y == 0:
        return 'Деление на ноль невозможно'
    else:
        return x / y

print(division(a, b))

