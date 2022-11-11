from abc import ABC, abstractclassmethod
import math

class Shape(ABC):
    @abstractclassmethod
    def area() -> float:
        pass

class Square(Shape):
    def __init__(self, lenght: int) -> None:
        self.length = lenght

    @classmethod
    def of(cls, length: int):
        return cls(length)

    def area(self):
        return pow(self.length, 2)


class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.radius = radius

    @classmethod
    def of(cls, radius: int):
        return cls(radius)

    def area(self):
        return math.pi * pow(self.radius, 2)


class Area:
    def sum(self, shapes) -> float:
        return sum([shape.area() for shape in shapes])
