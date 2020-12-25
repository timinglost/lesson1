user_name = str(input('Введите имя '))
user_surname = str(input('Введите фамилию '))
user_year = str(input('Введите год рождения '))
user_city = str(input('Введите город проживания '))
user_email = str(input('Введите email '))
user_telephone = str(input('Введите телефон '))
def user_data(name, surname, year, city, email, telephone):
    return 'Имя: ' + name + ', фамилия: ' + surname + ', год рождения: ' + year + ', город проживания: ' + city + ', email: ' + email + ', телефон: ' + telephone + '.'
print(user_data(name=user_name, surname=user_surname, year=user_year, city=user_city, email=user_email, telephone=user_telephone))
