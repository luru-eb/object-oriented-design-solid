from dataclasses import dataclass


@dataclass(frozen=True)
class Intensity:
    value: int

    def __post_init__(self):
        if (self.intensity < 0 or self.intensity > 255):
            raise ValueError('Intensity should be between 0 and 255')


class Color:
    def __init__(self, red: int, green: int, blue: int) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    @classmethod
    def white(cls):
        return cls(255, 255, 255)
    
    @classmethod
    def from_rgb(cls, red: Intensity, green: Intensity, blue: Intensity):
        return cls(red.value, green.value, blue.value)

    @classmethod
    def from_hex(cls, hex: str):
        value = hex.lstrip('#')
        return cls(int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16))
    
    def __eq__(self, other): 
        if not isinstance(other, Color):
            return NotImplemented

        return self.red == other.red and self.green == other.green and self.blue == other.blue