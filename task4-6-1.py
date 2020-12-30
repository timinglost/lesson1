from itertools import count
user_number = int(input('Введите число меньше 20 '))
i = user_number
while i <= 20:
    for i in count(i):
        print(i)
        i += 1
        break
