from random import shuffle, choice, uniform
class LotoCard:
    def __init__(self, name):
        self.name = name
        self.card_list = f'- карточка {self.name} -\n'
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
            i = 0
            self.card_list += ' '
            while i < 9:
                self.card_list += str(numb[i]) + ' '
                i += 1
            self.card_list += '\n'
            n += 1
        self.card_list += '----------------------'

class LotoGame:
    def __init__(self, player, computer):
        self.player = player.card_list
        self.computer = computer.card_list
        self.numb_list = [x for x in range(1, 91)]
        shuffle(self.numb_list)

    def start(self):
        n = 90
        while n > 0:
            number = choice(self.numb_list)
            index_number = self.numb_list.index(number)
            self.numb_list.pop(index_number)

            print(f'Новый боченок {number}. Осталось {n} попыток.')
            print(self.player)
            print(self.computer)
            player_list = self.player.split()
            i = 0
            player_list_new = []
            while i < len(player_list):
                try:
                    a = int(player_list[i])
                    player_list_new.append(a)
                    i += 1
                except ValueError:
                    i += 1
                    continue
            player_list = player_list_new

            computer_list = self.computer.split()
            i = 0
            computer_list_new = []
            while i < len(computer_list):
                try:
                    a = int(computer_list[i])
                    computer_list_new.append(a)
                    i += 1
                except ValueError:
                    i += 1
                    continue
            computer_list = computer_list_new

            answer = str(input('Зачеркнуть цифру? y/n '))
            if answer == 'y':
                if player_list.count(number) == 1:
                    self.player = self.player.replace(f' {number} ', ' - ')

                if player_list.count(number) == 0:
                    print('Вы проиграли(')
                    break
            if answer == 'n':
                if player_list.count(number) == 1:
                    print('Вы проиграли(')
                    break
                if player_list.count(number) == 0:
                    pass
            if computer_list.count(number) == 1:
                self.computer = self.computer.replace(f' {number} ', ' - ')
            if self.computer.count('-') == 39:
                print(self.player)
                print(self.computer)
                print('Вы проиграли(')
                break
            if self.player.count('-') == 39:
                print(self.player)
                print(self.computer)
                print('Вы выйграли!')
                break
            n -= 1

human_player = LotoCard('игрока')
computer_player = LotoCard('компьютера')
game = LotoGame(human_player, computer_player)
game.start()
