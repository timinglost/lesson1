file = open('task5-3.txt', encoding='utf-8')
n = len(file.readlines())
file.close()

file = open('task5-3.txt', encoding='utf-8')
x = 1
c = []
y = 0
while x <= n:
    a = file.readline().strip()
    b = a.split(' ')
    if float(b[1]) < 20000:
        c.append(b[0])
    y = y + float(b[1])
    x += 1
y = y / n
print(f'Фамилии сотрудников, которые имеют оклад менее 20 тыс {c}, средняя зп {y}')
file.close()
