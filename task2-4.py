user_str = str(input('Введите слова '))
my_list = []
a = 1
b = 0
my_list = user_str.split()
for i in my_list:
    if len(my_list[b]) <= 10:
        print(f'{a}  {my_list[b]}')
        b += 1
        a += 1
    else:
        print(f'{a} {my_list[b][0:10]}')
        b += 1
        a += 1


