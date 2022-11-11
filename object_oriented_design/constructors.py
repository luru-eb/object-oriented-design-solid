from haversine import (
    haversine,
    Unit
)


class Position:
    earth_radius_in_kilometers = 6371

    def __init__(self, latitude, longitude):
        if latitude < -90 or latitude > 90:
            raise ValueError('Latitude should be between -90 and 90')
        if longitude < -180 or longitude > 180:
            raise ValueError('Longitude should be between -180 and 180')

        self.latitude = latitude
        self.longitude = longitude

    def distance_in_kilometers_to(self, position):
        return haversine(
            (self.latitude, self.longitude),
            (position.latitude, position.longitude),
            unit=Unit.KILOMETERS
        )
    
    