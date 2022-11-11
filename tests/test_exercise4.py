import pytest

from exercises.exercise4 import Parrot, ParrotType


class TestParrot:
    def test_speed_of_european_parrot(self):
        parrot = Parrot(ParrotType.EUROPEAN, 0, 0, False)
        assert parrot.speed() == 12.0


    def test_speed_of_african_parrot_with_one_coconut(self):
        parrot = Parrot(ParrotType.AFRICAN, 1, 0, False)
        assert parrot.speed() == 3.0


    def test_speed_of_african_parrot_with_two_coconuts(self):
        parrot = Parrot(ParrotType.AFRICAN, 2, 0, False)
        assert parrot.speed() == 0.0


    def test_speed_of_african_parrot_with_no_coconuts(self):
        parrot = Parrot(ParrotType.AFRICAN, 0, 0, False)
        assert parrot.speed() == 12.0


    def test_speed_norwegian_blue_parrot_nailed(self):
        parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 1.5, True)
        assert parrot.speed() == 0.0


    def test_speed_norwegian_blue_parrot_not_nailed(self):
        parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 1.5, False)
        assert parrot.speed() == 18.0


    def test_speed_norwegian_blue_parrot_not_nailed_high_voltage(self):
        parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 4, False)
        assert parrot.speed() == 24.0
