revenue = float(input('Введите выручку '))
costs = float(input('Введите издержки '))
if revenue > costs:
    print('Предприятие прибольно')
    arrived = revenue - costs
    profitability_of_proceeds = (arrived / revenue) * 100
    print('Рентабельность выручки состовляет ', profitability_of_proceeds)
    staff = int(input('Введите количество сотрудников '))
    print('Прибыль фирмы в расчете на одного сотрудника ', arrived / staff)
else:
    print('Предприятие убыточно')