from time import sleep

class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зеленый']
    def running(self):
        n = int(input('Введите количество повторений '))
        i = 0
        while i < n:
            print(TrafficLight.__color[0])
            sleep(7)
            print(TrafficLight.__color[1])
            sleep(2)
            print(TrafficLight.__color[2])
            sleep(2)
            i += 1

a = TrafficLight()
a.running()