from attr import dataclass


@dataclass
class User:
    name: str
    last_name: str
    email: str


class MySqlRepository:
    def save(self, entity):
        pass


class CreateUser:
    def __init__(self) -> None:
        self.repository = MySqlRepository()

    def execute(self, user: User):
        self.repository.save(user)