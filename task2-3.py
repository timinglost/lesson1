user_number = int(input('Введите номер месяца '))
season = ['Зима', 'Осень', 'Лето', 'Весна']
season_dict = {1 : 'Зима',2 : 'Осень',3 : 'Лето',4 : 'Весна'}
if user_number == 1 or user_number == 2 or user_number == 12:
    print(season[0])
    print(season_dict[1])
elif user_number == 3 or user_number == 4 or user_number == 5:
    print(season[1])
    print(season_dict[2])
elif user_number == 6 or user_number == 7 or user_number == 8:
    print(season[2])
    print(season_dict[3])
elif user_number == 9 or user_number == 10 or user_number == 11:
    print(season[3])
    print(season_dict[4])
else:
    print('Введено некоректное число')
