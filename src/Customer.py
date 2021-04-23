from pydantic.dataclasses import dataclass
from typing import List
from src.Basket import Basket
from src.Giftcard import Giftcard
import dataclasses
import uuid

@dataclass
class Customer:
    basket: Basket = dataclasses.field(default_factory=lambda: Basket())
    name: str = None
    uuid: str = dataclasses.field(default_factory=lambda: uuid.uuid4())

    def add_gift_card(self, giftcards: List[Giftcard]):
        self.basket.add_giftcards(giftcards)

