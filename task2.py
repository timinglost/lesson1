
user_seconds = int(input('Введите секунды '))
hour = user_seconds // 3600
minutes = (user_seconds % 3600) // 60
seconds = (user_seconds % 3600) % 60
print(f'Время {hour}:{minutes}:{seconds}')
