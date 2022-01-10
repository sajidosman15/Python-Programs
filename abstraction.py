from abc import ABC,abstractmethod

class Shape(ABC):
    value=""
    @abstractmethod
    def display(self):
        pass


class Circle(Shape):

    def __init__(self,value):
        self.value=value

    def display(self):
        print(self.value)

a=Circle(10)
a.display()