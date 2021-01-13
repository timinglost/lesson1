#Первый способ посчитать линии:
my_file = open('task5-2.txt')
str_txt = (my_file.readlines())
numbers = len(str_txt)
print(f'Количество строк {numbers}')
my_file.close()
#Второй способ посчитать линии:
my_file = open('task5-2.txt')
print(f'Количество строк {len(my_file.readlines())}')
my_file.close()
# Подсчет слов
my_file = open('task5-2.txt')
n= len(my_file.readlines())
my_file.close()

my_file = open('task5-2.txt')
x = 1
while x <= n:
    a = my_file.readline()
    b = len(a.split(' '))
    print(f'Количество слов на {x} линии равно {b}')
    x += 1
my_file.close()
