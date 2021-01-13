f = open('task5-5.txt', 'w', encoding='utf-8')
user_number = str(input('Введите числа '))
f.write(user_number)
f.close()

f = open('task5-5.txt', encoding='utf-8')
a = (f.readline().split(' '))
n = len(a)
x = 0
c =0
while x < n:
    c = c + int(a[x])
    x += 1
print(f'Сумма = {c}')
f.close()