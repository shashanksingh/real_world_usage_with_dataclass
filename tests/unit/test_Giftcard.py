from decimal import Decimal
from unittest import TestCase
from unittest.mock import Mock

from src.Exceptions.InvalidDiscount import InvalidDiscount
from src.Domain.Giftcard import Giftcard


class TestGiftcard(TestCase):

    def test_calculate_discounted_price_with_10_Percent_Off(self):
        giftcard = Giftcard() \
            .with_product(Mock()) \
            .with_discount_percentage(Decimal(10.00)) \
            .with_face_value(Decimal(10.00)) \
            .build()
        assert giftcard.get_discount_price() == Decimal(9.00)

    def test_update_discount_percentage_with_out_of_bound_value(self):
        with self.assertRaises(InvalidDiscount):
            Giftcard()\
                .with_product(Mock()) \
                .with_discount_percentage(Decimal(999.00)) \
                .with_face_value(Decimal(10.00)) \
                .build()
