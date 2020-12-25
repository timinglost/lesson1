a = int(input('Введите действтельное положительное число '))
b = int(input('Введите целое отрицательное число '))
def my_func_1(x, y):
    return 1 / (x ** abs(y))
def my_func_2(x, y):
    c = 1
    z = x
    y = abs(y)
    while c < y:
        z = z * x
        c += 1
        break
    return 1 / z

print(my_func_1(a, b))
print(my_func_2(a, b))
