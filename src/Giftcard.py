from __future__ import annotations

from pydantic.dataclasses import dataclass
from decimal import Decimal
from src.Exceptions.InvalidDiscount import InvalidDiscount
from src.Product import Product


@dataclass
class Giftcard:
    product: Product = None
    face_value: Decimal = Decimal(0.0)
    discount_percentage: Decimal = Decimal(0.0)
    discounted_price: Decimal = Decimal(0.0)

    def __discount_percentage_must_be_withing_zero_and_100(self):
        if self.discount_percentage > 100 or self.discount_percentage < 0:
            raise InvalidDiscount("Discount must be withing 0 and 100")

    def __calculate_discounted_price(self) -> Decimal:
        return ((Decimal(100.00) - self.discount_percentage)  / Decimal(100.00) ) * self.face_value

    def update_discount_percentage(self, discount_percentage: Decimal):
        self.discount_percentage = discount_percentage
        self.discounted_price = self.calculate_discounted_price()

    def get_discount_price(self) -> Decimal:
        return self.discounted_price

    def with_product(self, product) -> Giftcard:
        self.product = product
        return self

    def with_face_value(self, face_value) -> Giftcard:
        self.face_value = face_value
        return self

    def with_discount_percentage(self, discount_percentage) -> Giftcard:
        self.discount_percentage = discount_percentage
        return self

    def build(self) -> Giftcard:
        self.__discount_percentage_must_be_withing_zero_and_100()
        self.discounted_price = self.__calculate_discounted_price()
        return self
