user_products = []
user_input = []
analytics = ['name :', [], 'price :', [], 'quantity :', [], 'units :', []]
number = 1
while input('Добавить продукт? Напишите y/n ') == 'y':
    user_input = dict({
        'name': input('Введите название '),
        'price': input('Введите цену '),
        'quantity': input('Введите количество '),
        'units': input('Введите единицу измерения ')})
    analytics[1] = analytics[1] + ([user_input['name']])
    analytics[3] = analytics[3] + ([user_input['price']])
    analytics[5] = analytics[5] + ([user_input['quantity']])
    analytics[7] = analytics[7] + ([user_input['units']])
    user_products.append((number, user_input))
    number += 1
print(user_products)
print(analytics)