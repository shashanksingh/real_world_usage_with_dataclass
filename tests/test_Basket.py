from decimal import Decimal
from unittest import TestCase
from unittest.mock import Mock

from src.Basket import Basket
from unittest.mock import MagicMock

from src.Giftcard import Giftcard


class TestBasket(TestCase):
    def test_add_giftcards(self):
        giftcard = Mock()
        basket = Basket()
        basket.add_giftcards([giftcard])
        assert len(basket.giftcards) == 1

    def test_calculate_total_value(self):
        giftcard_1 = Giftcard()
        giftcard_2 = Giftcard()

        giftcard_1.get_discount_price = MagicMock(return_value=Decimal(10.00))
        giftcard_2.get_discount_price = MagicMock(return_value=Decimal(10.00))

        basket = Basket([giftcard_1 , giftcard_2])
        assert basket.calculate_total_value() == Decimal(20.00)

