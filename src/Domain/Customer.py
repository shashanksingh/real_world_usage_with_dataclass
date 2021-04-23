from pydantic.dataclasses import dataclass
from typing import List, Optional

from pydantic.types import UUID

from src.Domain.Basket import Basket
from src.Domain.Giftcard import Giftcard
import dataclasses
import uuid

@dataclass
class Customer:
    basket: Basket = dataclasses.field(default_factory=lambda: Basket())
    name: str = None
    uuid: Optional[UUID] = dataclasses.field(default_factory=lambda: str(uuid.uuid1()))

    def add_gift_card(self, giftcards: List[Giftcard]):
        self.basket.add_giftcards(giftcards)

