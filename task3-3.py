a = float(input('Введите первое число '))
c = float(input('Введите второе число '))
b = float(input('Введите третье число '))
def my_func(x, y, z):
    my_list = [x, y, z]
    sorted(my_list)
    one = my_list[1]
    tow = my_list[2]
    return one + tow
print(my_func(a, b, c))
