from abc import ABC, abstractmethod

from typing import TypeVar, Generic

I = TypeVar("I")
O = TypeVar("O")

class UseCase(ABC, Generic[I, O]):
    @abstractmethod
    async def execute(self, parameter: I) -> O:
        raise NotImplementedError