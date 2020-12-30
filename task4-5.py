from functools import reduce
my_list = [x for x in range(100, 1001) if x % 2 == 0]
x = 1
# способ через for
for i in my_list:
    x = x * my_list[my_list.index(i)]
print(x)
# способ через reduce
print(reduce(lambda a, b: a * b,  my_list))


