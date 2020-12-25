user_list = []
c = True
while c == True:
    user_str = str(input('Введите числа (Чтобы выйти из цикла введите n) '))
    user_list = user_list + user_str.split()
    b = 0
    a = 0
    while b < len(user_list):
        if user_list[b] == 'n':
            c = False
            break
        a = a + int(user_list[b])

        b += 1
    print('Сумма =', a)


