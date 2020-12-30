from math import factorial
def fact(x):
    a = 0
    while a < x:
        a += 1
        yield factorial(a)
n = int(input('Введите число '))
for el in fact(n):
    print(el)
