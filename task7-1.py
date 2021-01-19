class Matrix:
    def __init__(self, l):
        self.list1 = l
    def __str__(self):
        a= ''
        n = len(self.list1)
        n1 = len(self.list1[0])
        i = 0
        while i < n:
            b = 0
            while b < n1:
                a = a + str(self.list1[i][b]) + ' '
                b += 1
            a += '\n'
            i += 1
        return a
    def __add__(self, a):
        self.a = a
        n1 = len(self.list1)
        n2 = len(self.a)
        n11 = len(self.list1[0])
        n22 = len(self.a[0])
        if n1 != n2 or n11 != n22:
            print('Матрицы разныне!')
        else:
            i = 0
            n = 0
            while i < n1:
                n = 0
                while n < n11:
                    self.list1[i][n] = self.list1[i][n] + self.a[i][n]
                    n += 1
                i += 1


a = Matrix([[12, 32, 32, 23], [423, 23, 434, 4]])
print(a)

b = Matrix([[23, 23], [423, 23], [34, 65]])
print(b)

d = Matrix([[12, 32, 32], [423, 23, 434], [65, 56, 34]])
print(d)

c = [[12, 32, 32], [423, 23, 434], [65, 56, 34]]

d + c
a + c
print(d)
