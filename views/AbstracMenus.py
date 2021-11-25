from abc import ABC, abstractmethod


class AbstractMenu(ABC):
    def __init__(self):
        self.options = {}

    @abstractmethod
    def __str__(self):
        pass

class AbstractInteraction(AbstractMenu):
    def __init__(self) :
        super().__init__()
        self.repositories = {}

    def set_repositories(self, name: str, repository):
        self.repositories[name] = repository