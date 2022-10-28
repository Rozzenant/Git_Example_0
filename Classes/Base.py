from abc import ABC, abstractmethod

class Base(ABC):
    def __init__(self):
        self.S = None

    @abstractmethod
    def square(self):
        pass