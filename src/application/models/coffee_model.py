from tortoise import fields

from .base_model import BaseModel

class CoffeeModel(BaseModel):
    name = fields.TextField(max_length=16) #fields.CharField(unique=True, max_length=16)
    price = fields.IntField()#fields.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        table = "coffees"