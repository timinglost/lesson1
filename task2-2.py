user_number = int(input('Выберете длину списка '))
my_list = []
a = 0
b = 0
while user_number > a:
    my_list.append(input('Введите что-то '))
    a += 1
c = int(len(my_list) / 2)
a = 0
while c > a:
    my_list[b], my_list[b + 1] = my_list [b + 1], my_list[b]
    a += 1
    b += 2
print(my_list)

