from typing import Any
from blacksheep import json, FromJSON, Response
from blacksheep.server.controllers import get, post, APIController 

from ...domain.usecases import UseCase
from ...domain.entities import CoffeeInEntity, CoffeeOutEntity

class CoffeeController(APIController):
    @classmethod
    def version(cls) -> str:
        return "v1"
    
    @classmethod
    def route(cls) -> str:
        return "coffee"
    
    @get()
    async def get_all(
        self,
        use_case: UseCase[Any, list[CoffeeOutEntity]]
    ) -> Response:
        response = await use_case.execute(any)

        return json(response)
    
    @post()
    async def create(
        self,
        parameter: FromJSON[CoffeeInEntity], 
        use_case: UseCase[CoffeeInEntity, CoffeeOutEntity]
    ) -> Response:
        response = await use_case.execute(parameter.value)

        return json(response)