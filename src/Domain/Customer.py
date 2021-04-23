from pydantic.dataclasses import dataclass
from typing import List
from src.Domain.Basket import Basket
from src.Domain.Giftcard import Giftcard
import dataclasses
import uuid

@dataclass
class Customer:
    uuid: str = dataclasses.field(default_factory=lambda: str(uuid.uuid4()))
    basket: Basket = dataclasses.field(default_factory=lambda: Basket())
    name: str = None

    def add_gift_card(self, giftcards: List[Giftcard]):
        self.basket.add_giftcards(giftcards)

