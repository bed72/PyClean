
from typing import Any
from blacksheep import Application

from ..controllers import CoffeeController

from ...external.di import handler_di
from ...external.database import handler_database

app = Application(show_error_details=True)

handler_di(app)
handler_database(app)

app.register_controllers([CoffeeController])