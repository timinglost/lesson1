from itertools import cycle
my_list = [19, 'lol', True, 666, 'yes']
user_number = int(input('Введите число '))
i = 1
for x in cycle(my_list):
    print(x)
    i += 1
    if i > user_number:
        break
