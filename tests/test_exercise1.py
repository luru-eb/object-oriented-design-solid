import pytest

from exercises.exercise1 import Person


class TestExercise1:
    def test_should_not_allow_invalid_emails(self):
        with pytest.raises(ValueError, match='Invalid email!'):
            Person(name='Test', email='test@eventbrite')

