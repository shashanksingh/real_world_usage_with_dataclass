from collections import defaultdict
from decimal import Decimal

from src.Domain.Customer import Customer
from src.Domain.Giftcard import Giftcard
from src.Domain.Product import Product

tesco_product = Product(name="Tesco")
google_play_product = Product(name="Google Play")

tesco_10_off_giftcard = Giftcard() \
    .with_product(tesco_product) \
    .with_face_value(Decimal(10.00)) \
    .with_discount_percentage(Decimal(10.00)) \
    .build()

google_play_90_off_giftcard = Giftcard() \
    .with_product(google_play_product) \
    .with_discount_percentage(Decimal(90.00)) \
    .with_face_value(Decimal(100.00)) \
    .build()

ALL_GIFTCARDS = [tesco_10_off_giftcard, google_play_90_off_giftcard]
ALL_CUSTOMERS = defaultdict(Customer)
