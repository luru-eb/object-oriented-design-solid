from abc import ABC, abstractmethod
from attr import dataclass


@dataclass
class User:
    name: str
    last_name: str
    email: str


class Repository(ABC):
    @abstractmethod
    def save(self, entity) -> None:
        pass


class MySqlRepository(Repository):
    def save(self, entity) -> None:
        pass


class InMemoryRepository(Repository):
    def __init__(self) -> None:
        self.entities = []

    def save(self, entity) -> None:
        self.entities.append(entity)


class CreateUser:
    def __init__(self, repository: Repository) -> None:
        self.repository = repository

    def execute(self, user: User):
        self.repository.save(user)