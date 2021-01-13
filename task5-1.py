my_file = open('task5-1.txt', 'w', encoding='utf-8')
user_txt = []
x = True
while x == True:
    user_text = (str(input('Введите текст ')))
    line = user_text + '\n'
    user_txt.append(line)
    if user_text == ' ':
        x = False
        user_txt.pop()
my_file.writelines(user_txt)
my_file.close()
