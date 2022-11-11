import pytest

from solid.open_closed_principle_after import Area, Circle, Square


class TestArea:
    def test_should_calculate_the_sum_of_the_areas_of_different_shapes(self):
        area = Area()
        sum = area.sum([
            Square.of(length=2),
            Circle.of(radius=2)
        ])
        assert sum == 16.566370614359172

