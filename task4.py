user_number = int(input('Введите челое положиельное число '))
number = 0
number_1 = 0
while user_number >= 0:
    number = user_number % 10
    user_number = user_number // 10
    if number >= number_1:
        number_1 = number
    break
print('Нибольшая цифра ', number_1)
