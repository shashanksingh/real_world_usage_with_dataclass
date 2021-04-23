from pydantic.dataclasses import dataclass
from decimal import Decimal
from typing import List
from src.Domain.Giftcard import Giftcard
import dataclasses


@dataclass
class Basket:
    giftcards: List[Giftcard] = dataclasses.field(default_factory=lambda: [])

    def add_giftcards(self, giftcards: List[Giftcard]):
        for giftcard in giftcards:
            self.giftcards.append(giftcard)

    def calculate_total_value(self) -> Decimal:
        return sum([giftcard.get_discount_price() for giftcard in self.giftcards])
