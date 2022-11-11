from haversine import haversine, Unit
from dataclasses import dataclass


@dataclass(frozen=True)
class Latitude:
    value: float

    def __post_init__(self):
        if self.value < -90 or self.value > 90:
            raise ValueError('Latitude should be between -90 and 90')


@dataclass(frozen=True)
class Longitude:
    value: float

    def __post_init__(self):
        if self.value < -180 or self.value > 180:
            raise ValueError('Longitude should be between -180 and 180')


class Position:
    earth_radius_in_kilometers = 6371

    def __init__(self, latitude: Latitude, longitude: Longitude):
        self.latitude = latitude
        self.longitude = longitude

    def distance_in_kilometers_to(self, position):
        return haversine(
            (self.latitude.value, self.longitude.value),
            (position.latitude.value, position.longitude.value),
            unit=Unit.KILOMETERS
        )
    
    