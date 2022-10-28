from Classes.Base import Base

class Square(Base):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.square()

    def __repr__(self):
        return f'Прямоугольник | {self.a}, {self.b} | и S = {self.S}'

    def square(self):
        self.S = self.a * self.b

    def __del__(self):
        print(f'Объект {self.__class__.__name__} удален')
        del self.a, self.b, self.S, self