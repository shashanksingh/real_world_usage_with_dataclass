from pydantic.dataclasses import dataclass
from typing import List
from src.Basket import Basket
from src.Giftcard import Giftcard
import dataclasses


@dataclass
class Customer:
    basket: Basket = dataclasses.field(default_factory=lambda: Basket())
    name: str = None

    def add_gift_card(self, giftcards: List[Giftcard]):
        self.basket.add_giftcards(giftcards)

