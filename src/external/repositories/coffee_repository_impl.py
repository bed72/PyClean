from uuid import UUID
from datetime import datetime
from typing import Any, Optional

from ...application.models import CoffeeModel

from ...domain.repositories import CoffeeRepository
from ...domain.entities import CoffeeInEntity, CoffeeOutEntity

class CoffeeRepositoryImpl(CoffeeRepository):
    def __init__(self, model: CoffeeModel) -> None:
        self._model = model

    async def get_all(self) -> list[CoffeeOutEntity]:
        response = await self._model.all()

        return list(
            map(lambda model: self._to_entity(model), response)
        )
    
    async def get(self, id: UUID) -> Optional[CoffeeOutEntity]:
        model = await self._model.filter(id).first()

        return self._to_entity(model)
    
    async def create(self, data: CoffeeInEntity) -> CoffeeOutEntity:
        model = await self._model.create(name=data.name, price=data.price)

        return self._to_entity(model)
    
    async def update(self, id: UUID, data: CoffeeInEntity) -> Optional[CoffeeOutEntity]:
        model = await self.get(id)

        if model == None: return None

        model.name = data.name
        model.price = data.price
        model.updated = datetime.now

        response = await self._model.update_or_create(model)

        return self._to_entity(response[0]) if response[1] else None

    async def delete(self, id: UUID) -> Any:
        await self._model.delete(id)

    def _to_entity(self, model: CoffeeModel) -> Optional[CoffeeOutEntity]:
       return CoffeeOutEntity(
           id=model.id, 
           name=model.name, 
           price=model.price, 
           created=model.created, 
           updated=model.updeted
        ) if model != None else None