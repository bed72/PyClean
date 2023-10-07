from tortoise import fields
from tortoise.models import Model

class BaseModel(Model):
    id = fields.UUIDField(pk=True)
    created = fields.DatetimeField(null=True, auto_now_add=True)
    updeted = fields.DatetimeField(null=True, auto_now_add=True)