import pytest

from object_oriented_design.named_constructors import Color, Intensity


class TestColor:
    def test_should_allow_to_convert_from_hexadecimal(self):
        white_color = Color.white()
        white_color_from_hex = Color.from_hex('#FFFFFF')
        assert white_color == white_color_from_hex