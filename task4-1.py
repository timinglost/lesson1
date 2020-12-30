import sys
time, rate, prize = sys.argv[1:]


print(f'Время работы {time}, ставка {rate} и премия {prize}')
my_sum = (int(time) * int(rate)) + int(prize)
print(f'Зарплета = {my_sum}')
