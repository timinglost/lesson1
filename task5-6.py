f = open('task5-6.txt', encoding='utf-8')
n = len(f.readlines())
f.close()
education = {}
x = 0
f = open('task5-6.txt', encoding='utf-8')
while x < n:
    a = f.readline().split(':')
    b = a[1]
    list = []
    i = 0
    l = len(b)
    z = ''
    while i < l:
        c = b[i]
        if '0' <= c <= '9':
            z += c
        elif c == '(':
            z = int(z)
            list.append(z)
            z = ''
        i += 1
    b = sum(list)
    education[a[0]] = b
    x += 1
print(education)
f.close()
