from typing import Any

from ...domain.usecases import UseCase
from ...domain.entities import CoffeeOutEntity
from ...domain.repositories import CoffeeRepository

class GetCoffeesUseCase(UseCase[Any, list[CoffeeOutEntity]]):
    def __init__(self, repository: CoffeeRepository) -> None:
        self._repository = repository

    async def execute(self, _: Any) -> list[CoffeeOutEntity]:
        return await self._repository.get_all()
