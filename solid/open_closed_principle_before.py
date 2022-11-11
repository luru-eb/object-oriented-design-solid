import math


class Square:
    def __init__(self, lenght: int) -> None:
        self.length = lenght

    @classmethod
    def of(cls, length: int):
        return cls(length)


class Circle:
    def __init__(self, radius: int) -> None:
        self.radius = radius

    @classmethod
    def of(cls, radius: int):
        return cls(radius)


class Area:
    def sum(self, shapes) -> float:
        areas = []
        for shape in shapes:
            if isinstance(shape, Square):
                areas.append(pow(shape.length, 2))
            elif isinstance(shape, Circle):
                areas.append(math.pi * pow(shape.radius, 2))
        
        return sum(areas)
