from blacksheep.server import Application

from tortoise.contrib.blacksheep import register_tortoise

def handler_database(app: Application):
    register_tortoise(
        app,
        generate_schemas=True,
        db_url="sqlite://database.sqlite3",
        modules={"models": ["src.application.models"]},
    )