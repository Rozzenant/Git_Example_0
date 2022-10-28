from abc import ABC, abstractmethod


class Base(ABC):
    def __init__(self):
        self.a = None
        self.b = None
        self.S = None

    @abstractmethod
    def square(self):
        return self.S

def main(status):
    print(status)

if __name__ == '__main__':
    main('Success - code 0')


