from random import shuffle, choice, uniform
class LotoCard:
    def __init__(self, name):
        self.name = name
        self.card_list = []
        self.numb_list = [x for x in range(1, 91)]
        shuffle(self.numb_list)
        n = 0
        while n < 3:
            numb = []
            i = 0
            while i < 5:
                numb.append(self.numb_list[0])
                self.numb_list.pop(0)
                i += 1
            numb.sort()
            i = 0
            while i < 4:
                a = round(uniform(0, len(numb)))
                numb.insert(a, ' ')
                i += 1
            self.card_list.append(numb)
            n += 1

class LotoGame:
    def __init__(self, player, computer):
        self.player = player.card_list
        self.computer = computer.card_list
        self.player_name = player.name
        self.computer_name = computer.name
        self.numb_list = [x for x in range(1, 91)]
        shuffle(self.numb_list)

    def start(self):
        p_w = 0
        c_w = 0
        n = 909
        while n > 0:
            number = choice(self.numb_list)
            index_number = self.numb_list.index(number)
            self.numb_list.pop(index_number)

            print(f'Новый боченок {number}. Осталось {n} попыток.')
            print(f'----карточка {self.player_name}----')
            i = 0
            while i < len(self.player):
                print(*self.player[i])
                i += 1
            print('-----------------------')
            print(f'--карточка {self.computer_name}--')
            i = 0
            while i < len(self.computer):
                print(*self.computer[i])
                i += 1
            print('-----------------------')

            answer = str(input('Зачеркнуть цифру? y/n '))
            answer1 = True
            if answer == 'y':
                if self.player[0].count(number) == 0 and self.player[1].count(number) == 0 and self.player[2].count(number) == 0:
                    answer1 = False
                i = 0
                while i < len(self.player):
                    if self.player[i].count(number) == 1:
                        a = self.player[i].index(number)
                        self.player[i][a] = '-'
                        p_w += 1
                    i += 1

            if answer == 'n':

                if self.player[0].count(number) == 1 or self.player[1].count(number) == 1 or self.player[2].count(number) == 1:
                    answer1 = False


            if answer1 == False:
                print('Вы проиграли(')
                break
            i = 0
            while i < len(self.computer):
                if self.computer[i].count(number) == 1:
                    a = self.computer[i].index(number)
                    self.computer[i][a] = '-'
                    c_w += 1
                i += 1
            if c_w == 15:
                print(f'----карточка {self.player_name}----')
                i = 0
                while i < len(self.player):
                    print(*self.player[i])
                    i += 1
                print('-----------------------')
                print(f'--карточка {self.computer_name}--')
                i = 0
                while i < len(self.computer):
                    print(*self.computer[i])
                    i += 1
                print('-----------------------')
                print('Вы проиграли(')
                break
            if p_w == 15:
                print(f'----карточка {self.player_name}----')
                i = 0
                while i < len(self.player):
                    print(*self.player[i])
                    i += 1
                print('-----------------------')
                print(f'--карточка {self.computer_name}--')
                i = 0
                while i < len(self.computer):
                    print(*self.computer[i])
                    i += 1
                print('-----------------------')
                print('Вы выйграли!')
                break
            n -= 1

human_player = LotoCard('игрока')
computer_player = LotoCard('компьютера')
game = LotoGame(human_player, computer_player)
game.start()
