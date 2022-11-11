import pytest

from object_oriented_design.primitive_obsession import (
    Latitude,
    Position,
    Longitude
)


class TestPosition:
    def test_should_calculate_the_distance_in_kilometers_between_granada_and_madrid(self):
        granada = Position(Latitude(37.176487), Longitude(3.597929))
        madrid = Position(Latitude(40.4168), Longitude(3.70379))
        kilometers = granada.distance_in_kilometers_to(madrid)
        assert kilometers == 360.4235510029618

    def test_should_not_allow_to_create_a_position_with_invalid_latitude(self):
        with pytest.raises(ValueError, match='Latitude should be between -90 and 90') as error:
            Position(Latitude(181), Longitude(100))

    def test_should_not_allow_to_create_a_position_with_invalid_longitude(self):
        with pytest.raises(ValueError, match='Longitude should be between -180 and 180') as error:
            Position(Latitude(90), Longitude(200))