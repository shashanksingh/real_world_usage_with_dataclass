from unittest import TestCase

from src.Domain.Customer import Customer
from src.Domain.Giftcard import Giftcard


class TestCustomer(TestCase):
    def test_add_empty_gift_card(self):
        customer = Customer(name="Shashank")
        customer.add_gift_card([])

    def test_add_gift_card(self):
        customer = Customer(name="Shashank")
        giftcard = Giftcard()
        customer.add_gift_card([giftcard])