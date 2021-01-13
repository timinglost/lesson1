rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
f = open('task5-4.txt', encoding='utf-8')
n = len(f.readlines())
x = 1
a = []
f.close()
f = open('task5-4.txt', encoding='utf-8')
f_new = open('task5-4-1.txt', 'w', encoding='utf-8')
while x <= n:
    a.append(f.readline().split(' — '))
    a[x-1][0] = rus[a[x-1][0]]
    f_new.writelines(a[x-1][0])
    f_new.write(' — ')
    f_new.writelines(a[x - 1][1])
    x += 1
f.close()
print(a)
f_new.close()
