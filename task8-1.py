class Data:
    def __init__(self, ultra_mega_super_name_for_data):
        self.data = str(ultra_mega_super_name_for_data)
    @classmethod
    def re_data(cls, data):
        a = data.split('.')
        print(int(a[0]), int(a[1]), int(a[2]))
    @staticmethod
    def v_data(data):
        a = data.split('.')
        if 1 <= int(a[0]) <= 31:
            print('day right')
        else:
            print('day error')
        if 1 <= int(a[1]) <= 12:
            print('month right')
        else:
            print('month error')
        if 0 <= int(a[2]) <= 2021:
            print('year right')
        else:
            print('year error')

Data.re_data('23.04.2021')
Data.v_data('23.04.2021')
Data.v_data('23.0.2021')
Data.v_data('-23.04.2022')
