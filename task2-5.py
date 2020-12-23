my_list = [7, 5, 3, 3, 2]
user_number = int(input('Введите число '))
c = my_list.count(user_number)
a = 0
for i in my_list:
    if c >0:
        a = my_list.index(user_number)
        my_list.insert(a + 1, user_number)
        break
    else:
        my_list.insert(a, user_number)
        while my_list[a] < my_list[a + 1]:
            my_list[a], my_list[a + 1] = my_list[a + 1], my_list[a]
            a += 1
            if user_number == 1 or user_number == 0:
                my_list.append(user_number)
                break

        break
print(my_list)
