import json

f = open('task5-7.txt', encoding='utf-8')
n = len(f.readlines())
f.close()
list = []
a = {}
b = {}
f = open('task5-7.txt', encoding='utf-8')
x = 0
y = 0
sum = 0
while x < n:
    c = f.readline().strip().split(' ')
    profit = int(c[2]) - int(c[3])
    if profit > 0:
        y += 1
        sum +=profit
    a[c[0]] = profit
    x += 1
a_p = sum / y
b['average_profit'] = a_p
list.append(a)
list.append(b)
print(list)
f.close()
with open('task5-7.json', 'w') as j:
    json.dump(list, j)