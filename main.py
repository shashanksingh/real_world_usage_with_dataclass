from decimal import Decimal

from src.Customer import Customer
from src.Giftcard import Giftcard
from src.Product import Product


def create():
    tesco_product = Product(name="Tesco")
    google_play_product = Product(name="Google Play")

    tesco_10_off_giftcard = Giftcard() \
        .with_product(tesco_product) \
        .with_face_value(Decimal(10.00)) \
        .with_discount_percentage(Decimal(10.00)) \
        .build()

    google_play_90_off_giftcard = Giftcard()\
        .with_product(google_play_product)\
        .with_discount_percentage(Decimal(90.00))\
        .with_face_value(Decimal(100.00))\
        .build()

    shashank_customer = Customer(name="Shashank")
    another_shashank_customer = Customer(name="AnotherShashank")

    shashank_customer.add_gift_card(
        [
            tesco_10_off_giftcard,
            tesco_10_off_giftcard
        ]
    )
    another_shashank_customer.add_gift_card(
        [
            tesco_10_off_giftcard,
            google_play_90_off_giftcard
        ]
    )



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create()
