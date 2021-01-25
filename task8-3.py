class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

digit = []
while True:
    user_int = input('Ведите число ')
    if user_int == 'stop':
        break
    try:
        if not user_int.isdigit():
            raise MyError('Не вводите строки, Вводите числа!')
    except MyError as d:
        print(d)
    else:
        digit.append(int(user_int))
print(digit)