import numbers
from abc import ABC
from uuid import UUID
from typing import Optional
from datetime import datetime
from dataclasses import dataclass

@dataclass
class CoffeeInEntity:
    name: str
    price: numbers

@dataclass
class CoffeeOutEntity:
    id: UUID
    name: str
    price: numbers
    created: Optional[datetime] = None
    updated: Optional[datetime] = None