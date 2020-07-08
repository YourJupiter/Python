import math


class Shape:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return self.__class__.__name__


class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def get_perimeter(self):
        return 2 * math.pi * self.r

    def get_area(self):
        return math.pi * self.r ** 2

    def __str__(self):
        return f"{super().__str__()}, r={self.r}"


class Triangle(Shape):

    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def __str__(self):
        return f"{super().__str__()}, a={self.a}, b={self.b}, c={self.c}"


class Rectangle(Shape):

    def get_perimeter(self):
        return 2 * self.a + 2 * self.b

    def get_area(self):
        return self.a * self.b

    def __str__(self):
        return f"{super().__str__()}, a={self.a}, b={self.b}"

def run():
    print('Оберіть свою фігуру:\n'
          '1. Прямокутник;\n'
          '2. Коло;\n'
          '3. Прямокутний трикутник;\n'
          '4. Stop\n'
          'Введіть номер:')
    n = input()
    if n == '1':
        print('Введіть довжину сторони а:')
        a = int(input()) 
        print('Введіть довжину сторони b:')
        b = int(input())
        rectangle = Rectangle(a, b)
        print('Оберіть що ви хочете знайти:\n'
          '1. Периметр;\n'
          '2. Площа;\n'
          '3. Stop\n'
          'Введіть номер:')
        m = input()
        if m == '1':
            print(rectangle.get_perimeter())
        elif m == '2':
            print(rectangle.get_area())
        elif m == '3':
            exit()
        else:
            print('Перевірте правильність вказаного номеру.')
    elif n == '2':
        print('Введіть радіус кола:')
        r = int(input())
        circle = Circle(r)
        print('Оберіть що ви хочете знайти:\n'
          '1. Периметр;\n'
          '2. Площа;\n'
          '3. Stop\n'
          'Введіть номер:')
        m = input()
        if m == '1':
            print(circle.get_perimeter())
        elif m == '2':
            print(circle.get_area())
        elif m == '3':
            exit()
        else:
            print('Перевірте правильність вказаного номеру.')
    elif n == '3':
        print('Введіть довжину катета а:')
        a = int(input()) 
        print('Введіть довжину катета b:')
        b = int(input())
        print('Введіть довжину гіпотенузи c:')
        c = int(input())
        triangle = Triangle(a, b, c)
        print('Оберіть що ви хочете знайти:\n'
          '1. Периметр;\n'
          '2. Площа;\n'
          '3. Stop\n'
          'Введіть номер:')
        m = input()
        if m == '1':
            print(triangle.get_perimeter())
        elif m == '2':
            print(triangle.get_area())
        elif m == '3':
            exit()
        else:
            print('Перевірте правильність вказаного номеру.')
    elif n == '4':
        exit()
    else:
        print('Перевірте правильність вказаного номеру.')

while True:
    run()
