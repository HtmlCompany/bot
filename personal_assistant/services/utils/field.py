from abc import ABC, abstractmethod
from typing import Any


class Field(ABC):
    def __init__(self, value: str):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @staticmethod
    @abstractmethod
    def _value_validation(value: str) -> Any:
        pass

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value!r})"
