my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [x for x in my_list if my_list[my_list.index(x)] > my_list[my_list.index(x) - 1] and my_list.index(x) > 0]
print(new_list)
