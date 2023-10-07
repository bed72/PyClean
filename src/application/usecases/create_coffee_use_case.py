from ...domain.usecases import UseCase
from ...domain.repositories import CoffeeRepository
from ...domain.entities import CoffeeInEntity, CoffeeOutEntity

class CreateCoffeeUseCase(UseCase[CoffeeInEntity, CoffeeOutEntity]):
    def __init__(self, repository: CoffeeRepository) -> None:
        self._repository = repository

    async def execute(self, parameter: CoffeeInEntity) -> CoffeeOutEntity:
        return await self._repository.create(parameter)
