from abc import ABC, abstractmethod


class AbstractMenu(ABC) :
    def __init__(self) :
        self.options = {}

    @abstractmethod
    def __str__(self) :
        pass
