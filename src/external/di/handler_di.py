from typing import Any
from blacksheep.server import Application

from ...application.models import CoffeeModel
from ...domain.entities import CoffeeInEntity, CoffeeOutEntity 

from ...domain.repositories import CoffeeRepository
from ..repositories import CoffeeRepositoryImpl

from ...domain.usecases import UseCase
from ...application.usecases import GetCoffeesUseCase, CreateCoffeeUseCase

def handler_di(app: Application):
    app.services.add_scoped(CoffeeModel)
    app.services.add_scoped(CoffeeRepository, CoffeeRepositoryImpl)
    app.services.add_scoped(UseCase[Any, list[CoffeeOutEntity]], GetCoffeesUseCase)
    app.services.add_scoped(UseCase[CoffeeInEntity, CoffeeOutEntity], CreateCoffeeUseCase)
