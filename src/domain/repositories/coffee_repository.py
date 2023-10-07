from uuid import UUID
from typing import Any, Optional
from abc import ABC, abstractmethod

from ..entities import CoffeeInEntity, CoffeeOutEntity

class CoffeeRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[CoffeeOutEntity]:
        raise NotImplementedError
    
    @abstractmethod
    async def get(self, id: UUID) -> Optional[CoffeeOutEntity]:
        raise NotImplementedError
    
    @abstractmethod
    async def create(self, data: CoffeeInEntity) -> CoffeeOutEntity:
        raise NotImplementedError
    
    @abstractmethod
    async def update(self, id: UUID, data: CoffeeInEntity) -> Optional[CoffeeOutEntity]:
        raise NotImplementedError
    
    @abstractmethod
    async def delete(self, id: UUID) -> Any:
        raise NotImplementedError