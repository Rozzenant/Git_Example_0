from Classes.Base import Base
from math import sqrt

class Triangle(Base):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.square()

    def __repr__(self):
        return f'Треугольник | {self.a}, {self.b}, {self.c} | и S = {round(self.S, 3)}'

    def square(self):
        p = (self.a + self.b + self.c) / 2
        self.S = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def __del__(self):
        print(f'Объект {self.__class__.__name__} удален')
        del self.a, self.b, self.c, self.S, self